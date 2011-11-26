from Tsoha.forms import AddRecipeForm

class AddRecipeValidator():
    def __init__(self, request):
        self.request = request
                

    def hasRequiredFields(self,form):
        name = form.cleaned_data['drink_name']
        recipe = form.cleaned_data['drink_recipe']  
        if recipe and name:
            return True
        return False
       
    def isValidAddRecipeRequest(self):
        if self.request.method == 'POST':
            form = AddRecipeForm(self.request.POST) 
            if form.is_valid():
                return True
        return False
               
