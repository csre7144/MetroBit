from django.shortcuts import render,HttpResponse,redirect
from contact.forms import ContactList
from django.contrib import messages
from achievement.models import achievement
from team.models import TeamList
from career.forms import careerList

# Create your views here.
def home(request):
      return render(request, 'index.html')

def about(request):
      return render(request, 'about.html')

def career(request):
    if request.method == 'POST':
        form = careerList(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request,'Your application has successfully. We will get back to you as soon as possible.')
            return redirect('thankyou')
    else:
        form = careerList()
    context = {
          'form': form,
          
    }
    return render(request, 'career.html', context)

def thankyou(request):
      return render(request, 'careerty.html')

def team(request):
      teams = TeamList.objects.all()
      return render(request, 'teams.html', {'teams': teams})

def contact(request):
      if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            data = ContactList(name=name, email=email, phone=phone, message=message)
            data.save()
            messages.success(request,'Your application has successfully. We will get back to you as soon as possible.')
      return render(request, 'contact.html')

def achievements(request):
      achieve = achievement.objects.all()
      return render(request, 'achieve.html', {'achieve':achieve})

def lenovo(request):
      return render(request, 'lenovo_product.html')

def thinkbook(request):
      return render(request, 'thinkbook.html')

def thinkbook14(request):
      return render(request, 'thinkbook14.html')

def thinkbook15(request):
      return render(request, 'thinkbook15.html')

def thinkpad(request):
      return render(request, 'thinkpad.html')

def thinkpade14(request):
      return render(request, 'thinkpadE14.html')

def thinkpade15(request):
      return render(request, 'thinkpadE15.html')

def yoga(request):
      return render(request, 'yoga.html')

def desktoplist(request):
      return render(request, 'desktoplist.html')

def thinkcentre30(request):
      return render(request, 'tc_neo30.html')

def thinkcentre50t(request):
      return render(request, 'tc_neo50.html')

def thinkcentre50s(request):
      return render(request, 'tc_neo50s.html')

def thinkcentre50q(request):
      return render(request, 'tc_neo50q.html')

def thinkcentre70t(request):
      return render(request, 'tc_neo70t.html')

def thinkcentre70q(request):
      return render(request, 'tc_neo70q.html')

def workstation(request):
      return render(request, 'workstation.html')

def thinkpadp14s(request):
      return render(request, 'm_p14.html')

def thinkpadp15v(request):
      return render(request, 'm_p15.html')

def thinkpadp16v(request):
      return render(request, 'm_p16.html')

def thinkstationp360(request):
      return render (request, 'm_p360.html')

def thinkstationtiny(request):
      return render (request, 'm_p360tiny.html')

def tabletlist(request):
      return render(request, 'tabletlist.html')

def m7(request):
      return render(request, 'm7.html')

def m8(request):
      return render(request, 'm8.html')

def m9(request):
      return render(request, 'm9.html')

def m10(request):
      return render(request, 'm10.html')

def m11(request):
      return render(request, 'm11.html')

def k10(request):
      return render(request, 'k10.html')

def k11(request):
      return render(request, 'k11.html')

def p11(request):
      return render(request, 'p11.html')

def p12(request):
      return render(request, 'p12.html')

def displaylist(request):
      return render(request, 'displaylist.html')

def c19(request):
      return render(request, 'c19.html')

def e20(request):
      return render(request, 'e20.html')

def s22e(request):
      return render(request, 's22e.html')

def s24e20(request):
      return render(request, 's24e20.html')

def s24i30(request):
      return render(request, 's24i30.html')

def t24t(request):
      return render (request, 't24t.html')

def t24v(request):
      return render(request, 't24v.html')

def t27i(request):
      return render (request, 't27i.html')

def netgear_us(request):
      return render(request, 'netgear_u_s.html')

def netgear_ms(request):
      return render(request, 'netgear_m_s.html')

def netgear_router(request):
      return render(request, 'netgear_router.html')

def netgear_ap(request):
      return render(request, 'netgear_ap.html')

def benqled(request):
      return render(request, 'benqled.html')

def benq_eyecare(request):
      return render(request, 'benq_eyecare.html')

def benq_premium(request):
      return render(request, 'benq_premium.html')

def benq_mobiuz(request):
      return render(request, 'benq_mobiuz.html')

def benq_zowie(request):
      return render(request, 'benq_zowie.html')

def benq_design(request):
      return render(request, 'benq_design.html')

def benq_professional(request):
      return render(request, 'benq_professional.html')

def benq_projector(request):
      return render(request, 'benqprojector.html')

def mx560(request):
      return render(request, 'mx560.html')

def mx560p(request):
      return render(request, 'mx560p.html')

def mw560(request):
      return render(request, 'mw560.html')

def mh560(request):
      return render(request, 'mh560.html')

def mx808pstplus(request):
      return render(request, 'mx808pstplus.html')

def mx8080pst(request):
      return render(request, 'mx808pst.html')

def mw809pst(request):
      return render(request, 'mw809pst.html')

def mw855ust(request):
      return render(request, 'mw855ust.html')

def benq_intercativity_display(request):
      return render(request, 'benqled_interact_display.html')

def re6503(request):
      return render(request, 're6503.html')

def rp6504(request):
      return render(request, 'rp6504.html')

def rm6503(request):
      return render(request, 'rm6503.html')

def benqled_cameralist(request):
      return render(request, 'benqled_cameralist.html')

def webcam(request):
      return render(request, 'webcam.html')

def camera(request):
      return render(request, 'camera.html')

def videobar(request):
      return render(request, 'videobar.html')

def pantum_productsingle(request):
      return render(request, 'pantum_productsingle.html')

def pantum_single3302(request):
      return render(request, 'pantum_single3302.html')

def pantum_single2518(request):
      return render(request, 'pantum_single2518.html')

def pantum_product(request):
      return render(request, 'pantum_product.html')

def pantum(request):
      return render(request, 'pantum.html')

def pantum_multi5100adn(request):
      return render(request, 'pantum_multi5100adn.html')

def pantum_multi7102(request):
      return render(request, 'pantum_multi7102.html')

def pantum_multi6518(request):
      return render(request, 'pantum_multi6518.html')

def network_cable(request):
      return render(request, 'network_cable.html')

def cctv_cable(request):
      return render(request, 'cctv_cable.html')

def cat6list(request):
      return render(request, 'cat6list.html')

def communicatelist(request):
      return render(request, 'communicatelist.html')

def sophoslist(request):
      return render(request, 'sophoslist.html')

def so87(request):
      return render(request, 'so87.html')

def so107(request):
      return render(request, 'so107.html')

def so116(request):
      return render(request, 'so116.html')

def so126(request):
      return render(request, 'so126.html')

def so136(request):
      return render(request, 'so136.html')


def so2100(request):
      return render(request, 'so2100.html')

def so2300(request):
      return render(request, 'so2300.html')

def so3100(request):
      return render(request, 'so3100.html')

def so3300(request):
      return render(request, 'so3300.html')

def so4300(request):
      return render(request, 'so4300.html')

def so4500(request):
      return render(request, 'so4500.html')

def so5500(request):
      return render(request, 'so5500.html')

def so6500(request):
      return render(request, 'so6500.html')

def qnaplist(request):
      return render(request, 'qnaplist.html')

def ts233(request):
      return render(request, 'ts233.html')

def ts433(request):
      return render(request, 'ts433.html')

def ts462(request):
      return render(request, 'ts462.html')

def ts664(request):
      return render(request, 'ts664.html')

def ts453e(request):
      return render(request, 'ts453e.html')

def ts473a(request):
      return render(request, 'ts473a.html')

def ts873a(request):
      return render(request, 'ts873a.html')

def bl(request):
      return render(request, 'brandslive.html')