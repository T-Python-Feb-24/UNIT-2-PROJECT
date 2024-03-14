from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

properties = [
        {"title" : "المنطقه الشماليه", "image" : "coffee1.jpeg", "id" : "p1", "content" : " بداية مع حمسة المنطقة الشمالية تتميز حمستها بالحمسة الغامقة، حيث يحمس بن القهوة الشمالية مع الهيل والقرنفل والذي يزيد من دكانتها، وعادة ما يكون التحميس الغامق عند وضعه على النار لمدة 30 دقيقة أي نصف ساعة، والذي يعكس طعماً مراً وطعم التدخين، والذي يساهم بالتقليل من نسبة الكافيين."},
        {"title" : "المنطقة الجنوبية", "image" : "coffee2.jpeg", "id" : "p2", "content" : "أما المنطقة الجنوبية من المملكة العربية السعودية، تكون حمسة بن القهوة السعودية متوسط، كما أنه يحمس مع النانخة أو القرفة أو الزنجبيل، وتكون الحمسة وسط، أي أنها تحرك على النار لمدة تقارب 16 دقيقة أو الربع ساعة، ويكون هنا لون البن بنياً متوسطاً، ويكون المذاق متوازن بين الحموضة وحلوة المذاق قليلاً، وهنا يكون معدل الكافيين متوسطاً..الجدير بالذكر أن النانخة هي الكراوي كما يسميها بعض مناطق المملكة، وهي نبتة سنوية، تشبة أوراق نبات الخلة، وهي ذات مذاق حار نوعاً ما."},
        {"title" : "المنطقة الغربيه", "image" : "coffee3.jpg", "id" : "p3",'content': 'بنفس السياق نتعرف على حمسة المنطقة الغربية فتتميز قهوتهم بالحمسة الفاتحة وتحمس مع الهيل وقد يضاف إليها القرنفل أو بخور المستكة، حيث يكون الحمس المتوسط لبن القهوة الفاتح لمدة لا تزيد عن 9 دقائق، وما يميزها اللون الأشقر وحموضة زائدة، ونكهة فاكهة البن واضحة، بالإضافة إلى أن يكون معدل الكافيين بها عالياً.'},
        {"title" : "المنطقة الشرقية", "image" : "coffee4.jpg", "id" : "p4",'content':'كذلك أيضاً حمسة بن القهوة السعودية للمنطقة الشرقية فاتحة اللون والتي لا تزيد عن مدة 9 دقائق حتى لا يتغير لونها ويتم الحفاظ على لونها الفاتح، ويتم إضافة الهيل وأيضاً الزعفران.'},
         {"title" : "المنطقة الوسطى", "image" : "coffee7.webp", "id" : "p5",'content':'وختاماً مع حمسة المنطقة الوسطى (النجدية) لبن القهوة السعودية تكون فاتحة أيضاً، على غرار المنطقة الغربية والشرقية، ويضاف لها الهيل والقرنفل أو الزعفران. الجدير بالذكر أن الزعفران هو تجفيف المياسم وهو جزء من أقلام زهرة الزعفران الخريف البنفسجي، يضفي صبغاً أصفر ذا لون زاهٍ، ويستخدم أيضاً لإضافة نكهة على الطعام'}
       

       
    ]

def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')

def contact_Basic(request:HttpRequest):
    return render (request, "main/contact_page.html")

def type_Basic(request:HttpRequest):
    context = {'properties':properties}
    return render (request, "main/type_page.html", context)

def read_Basic(request:HttpRequest):
    return render (request, "main/read_page.html")

def resource_Basic(request:HttpRequest):
    return render (request, "main/resource_page.html")


def test_Basic(request:HttpRequest):
    return render (request, "main/test.html")

def dark_mode(request:HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "True", max_age=60*60*24*7)

    return response

def light_mode(request:HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("DarkMode", "False")

    return response

# Create your views here.
