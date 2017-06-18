from django.test import TestCase, Client
from .models import Ramo, Profe

# Create your tests here.

class U_ramos_test(TestCase):
    def test_link_to_form_exists(self):
        #arrange
        client = Client()
        #act
        response = client.get("/") #solo va a existir 1 pagina, la base
        #assert
        self.assertIn('href="https://docs.google.com/forms/d/e/1FAIpQLSe9qTLE9DG_vNgCiXWw55yySYuZ72n2w-eOuya4LasE04MXRg/viewform?c=0&w=1"',response.content)
        
    def test_select_ramo_exists(self):
        #arrange
        client = Client()
        #act
        response = client.get("/") #solo va a existir 1 pagina, la base
        #assert
        self.assertIn('id="select_ramos"',response.content) #tiene que existir alguna componente que tenga el id select_ramos
    
    def test_select_ramo_shows_ramos(self):
        #arrange
        client = Client()
        r1 = Ramo.objects.create(name="Ramo 1", code="CC0000")
        r2 = Ramo.objects.create(name="Ramo 2", code="CC0001")
        r3 = Ramo.objects.create(name="Ramo 3", code="CC0002")
        #act
        response = client.get("/") #solo va a existir 1 pagina, la base
        #assert
        
        self.assertIn('Ramo 1</option>',response.content)
        self.assertIn('Ramo 2</option>',response.content)
        self.assertIn('Ramo 3</option>',response.content)
    
    def test_select_profe_exists(self):
        #arrange
        client = Client()
        #act
        response = client.get("/") #solo va a existir 1 pagina, la base
        #assert
        self.assertIn('id="select_profes"',response.content) #tiene que existir alguna componente que tenga el id select_profes
        
    #si cambio el ramo cambia la lista de profes, este test no esta implementado
    def test_select_ramo_changes_select_profe(self):
        #arrange
        client = Client()
        r1 = Ramo.objects.create(name="Ramo 1", code="CC0000")
        r2 = Ramo.objects.create(name="Ramo 2", code="CC0001")
        r3 = Ramo.objects.create(name="Ramo 3", code="CC0002")
        
        p1 = Profe.objects.create(name="Profe 1")
        p1.ramos.add(r1,r2)
        p2 = Profe.objects.create(name="Profe 2")
        p2.ramos.add(r3)
        p3 = Profe.objects.create(name="Profe 3")
        p3.ramos.add(r3,r1)
        #act
        response = client.get("/") #solo va a existir 1 pagina, la base
        
        #assert
        self.assertIn('Ramo 1</option>',response.content)
        self.assertIn('Ramo 2</option>',response.content)
        self.assertIn('Ramo 3</option>',response.content)
        