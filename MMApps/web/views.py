from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password

from functools import wraps

from MMApps.clients.models import Clients
from MMApps.master.helpers.check_password import is_valid_password
from MMApps.master.helpers.JWTToken import create_jwt_token,decode_jwt_token

from .emailHelpers import send_activation_email

import time
import jwt

# def login_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         # Check if 'client_id' is in the session
#         if 'client_id' in request.session:
#             # The user is authenticated, proceed to the view
#             return view_func(request, *args, **kwargs)
#         else:
#             # The user is not authenticated, redirect to the login view
#             return redirect('login_view')
#     return _wrapped_view

class webView:
    def index_view(self, request):
        return render(request, 'web/index.html')
    
    def terms_of_service_view(self, request):
        return render(request, 'web/terms_and_condition.html')
    
class authView:    
    def login_view(self, request):
        if request.method == 'POST':
            email_ = request.POST['email']
            password_ = request.POST['password']

            if Clients.objects.filter(email=email_).exists():
                client = Clients.objects.get(email=email_)
                if client.is_active:
                    is_correct = check_password(password_, client.password)
                    if is_correct:
                        request.session['client_id'] = client.client_id
                        return redirect('index_view')
                    else:
                        messages.error(request, "Incorrect password.")
                        return redirect('login_view')
                else:
                    messages.info(request, "Your account is not active. Please activate it first.")
                    return redirect('login_view')
            else:
                messages.info(request, "Email does not exist.")
                return redirect('login_view')
        return render(request, 'web/login.html')
    
    def register_view(self, request):
        if request.method == 'POST':
            email_ = request.POST['email']
            mobile_ = request.POST['mobile']
            password_ = request.POST['password']
            confirm_password_ = request.POST['confirm_password']
            terms_and_condition_ = request.POST['t&c']

            if terms_and_condition_ == "on":
                terms_and_condition_ = True
            else:
                terms_and_condition_ = False

            
            if Clients.objects.filter(email=email_).exists():
                messages.info(request, "Email already exists. Please use a different email.")
                return redirect('register_view')
            else:
                if Clients.objects.filter(mobile=mobile_).exists():
                    messages.info(request, "Mobile number already exists. Please use a different mobile number.")
                    return redirect('register_view')
                    
                else:
                    if password_ != confirm_password_:
                        messages.info(request, "Password and confirm password does not match.")
                        return redirect('register_view')
                        
                    else:
                        is_valid, validation_message = is_valid_password(password_)
                        if not is_valid:
                            messages.info(request, validation_message) 
                            return redirect('register_view')
                        else:
                            new_client = Clients.objects.create(
                                email = email_,
                                mobile = mobile_,
                                password = password_,
                                is_verified_tac = terms_and_condition_
                            )
                            new_client.save()

                            client_data = {
                                'client_id':new_client.client_id,
                                'email':new_client.email,
                                'verification_token': create_jwt_token(new_client.client_id)
                            }
                            send_activation_email(request, client_data)
                            messages.success(request, "Registration successful! Please check your email to activate your account.")
                            return redirect('login_view')
        return render(request, 'web/signUp.html')
    
    def activate_account(self, request,client_id,token):
        print("1",client_id)
        print("2",token)
        try:
            # Decode the token
            payload = decode_jwt_token(token)
            print("3", payload)
            
            # Check if the customer ID in the payload matches the customer ID in the URL
            if payload['client_id'] != client_id:
                messages.error(request, "Invalid confirmation link.")
                return redirect('some_error_page')  # Redirect to an error page

            # Check if the token is expired
            if payload['exp'] < time.time():
                messages.error(request, "Confirmation link has expired.")
                return redirect('some_error_page')  # Redirect to an error page

            # Find the customer and activate the account
            customer = Clients.objects.get(client_id=client_id)
            customer.is_active = True  # Assuming you have an is_active field
            customer.save()

            messages.success(request, "Your account has been activated successfully.")
            return redirect('login_view')  # Redirect to the login page

        except jwt.ExpiredSignatureError:
            messages.error(request, "Confirmation link has expired.")
            return redirect('some_error_page')  # Redirect to an error page
        except jwt.InvalidTokenError:
            messages.error(request, "Invalid confirmation link.")
            return redirect('some_error_page')  # Redirect to an error page
        except Clients.DoesNotExist:
            messages.error(request, "Customer not found.")
            return redirect('some_error_page')  # Redirect to an error page

    def forgot_password(self, request):
        return render(request, 'web/forgot_password.html')
    
webViewObject = webView()
authViewObject = authView()