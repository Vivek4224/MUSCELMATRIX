from django.shortcuts import render

class webView:
    def index_view(self, request):
        return render(request, 'web/index.html')
    
webViewObject = webView()