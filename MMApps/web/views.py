from django.shortcuts import render

class webView:
    def index_view(self, request):
        return render(request, 'web/index.html')
    
class authView:    
    def login_view(self, request):
        return render(request, 'web/login.html')
    
    def register_view(self, request):
        return render(request, 'web/signUp.html')
    
webViewObject = webView()
authViewObject = authView()