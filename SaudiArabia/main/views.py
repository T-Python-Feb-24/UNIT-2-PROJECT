from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.urls import reverse


def home_page(request: HttpRequest):

    return render(request, "index.html")


def mode_light(request: HttpRequest):

    response = redirect("main:home_page")
    response.set_cookie("mode", "False")

    return response


def mode_dark(request: HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode", "True")

    return response


def properties_page(request: HttpRequest):
    properties = [
        {
            "name": "الإستراتيجية الوطنية للتقنية الحيوية",
            "image": ["DNA.jpg", "biotech-side.png"],
            "bref":
            '''
            تعزيزًا لمكانة المملكة كدولة رائدة في قطاع التقنية الحيوية، تجسد الاستراتيجية الوطنية للتقنية الحيوية،
            وتتسع آفاقها لتعبّر عن بداية رحلةٍ تحوليةٍ للمملكة وللعالم. 
            تستهدف الاستراتيجية أن تصبح المملكة تجمعاً عالمياً رائداً في مجال التقنية الحيوية،
            إلى جانب تحقيق مستوى عالٍ من الاكتفاء الذاتي وإحداث أثر اجتماعي واقتصادي إيجابي.
            ''',
            "url": reverse("main:nb_strategy"),
        },

        {
            "name": "نيوم",
            "image": ["neom_desktop-1.png"],
            "bref": "في عام 2017 أطلق صاحب السمو الملكي الأمير محمد بن سلمان بن عبدالعزيز ولي العهد رئيس مجلس الوزراء مشروع نيوم الجريء الذي يقوده صندوق الاستثمارات العامة، ليحول الصحراء إلى مدينة مستقبلية مبتكرة في شمال غرب المملكة، تعمل بنسبة 100% بالطاقة المتجددة، لتكون نموذجًا جديدًا للحياة المستدامة والعمل والازدهار، حيث يمكن البشرية من التقدم دون المساس بصحة كوكب الأرض.",
            "url": reverse("main:nb_strategy"),
        },

        {
            "name": "أوكساجون",
            "image": ["oxagon.png"],
            "bref": '''هي المدينة الساحلية الصناعية العائمة في نيوم، التي ستربطكم مباشرة بالأسواق العالمية.
            \nتبني أوكساچون منظومة صناعية متقدمة ونظيفة تراعي مبادئ الحفاظ على البيئة، وتسرّع التحول إلى الثورة الصناعية الرابعة ومبادئ الاقتصاد الدائري. أوكساچون هي فرصة جديدة تُبنى من الصفر لتغيير مفهوم المدن الصناعية التقليدية، وإنشاء نموذج جديد يتمحور حول الإنسان والابتكار و الاستدامة.''',
            "url": reverse("main:nb_strategy"),
        },

        {
            "name": "الاستراتيجية الوطنية للاستثمار",
            "image": ["kafd.png"],
            "bref": '''
                تنمي الاستراتيجية الوطنية للاستثمار البيئة التنافسية السعودية وتصنع مستقبلًا أكثر إشراقًا للقطاعات الحيوية.
                   \n تسهم الاستراتيجية الوطنية للاستثمار التي أطلقها صاحب السمو الملكي الأمير محمد بن سلمان بن عبدالعزيز ولي العهد ورئيس مجلس الوزراء في دفع عجلة التنمية وتنويع الاقتصاد المحلي، حيث تستهدف زيادة مساهمة القطاع الخاص في الناتج المحلي الإجمالي، وجذب المزيد من الاستثمارات الأجنبية، وزيادة الصادرات غير النفطية، وتقليل البطالة، وتعزيز تصنيف المملكة بين أفضل عشرة اقتصادات في مؤشر التنافسية العالمية بحلول عام 2030.''',
            "url": reverse("main:nb_strategy"),
        },

        {
            "name": "صنع في السعودية",
            "image": ["saudi-contaner.png"],
            "bref": '''
            يحفز برنامج "صنع في السعودية" الشركات المحلية على توسيع نطاق أعمالها، والاستفادة من مزايا البرنامج لتسويق منتجاتها إلى عدد أكبر من العملاء، والتواصل مع المستهلكين المهتمين بالمنتجات والشركات السعودية.
            ''',
            "url": reverse("main:nb_strategy"),
        },
    ]

    context = {"properties": properties}

    return render(request, "properties.html", context)


def national_biotechnology_strategy(request: HttpRequest):

    return render(request, "nb_strategy.html")


def contactus_page(request: HttpRequest):
    return render(request, "contactus.html")
