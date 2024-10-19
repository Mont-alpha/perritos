from django.db import models

# Create your models here.

tipo_casa = (
    ('Departamento','Departamento'),
    ('Casa','Casa'),
    ('Parcela','Parcela')
)
sexo = (('Macho','Macho'),('Hembra','Hembra'))


lista_perros = ['Quiltro','Affenpinscher', 'Airedale terrier', 'Akita', 'Akita americano', 'Alaskan Husky', 'Alaskan malamute', 'American Foxhound', 'American pit bull terrier', 'American staffordshire terrier', 'Ariegeois', 'Artois', 'Australian silky terrier', 'Australian Terrier', 'Austrian Black & Tan Hound', 'Azawakh', 'Balkan Hound', 'Basenji', 'Basset Alpino (Alpine Dachsbracke)', 'Basset Artesiano Normando', 'Basset Azul de Gascuña (Basset Bleu de Gascogne)', 'Basset de Artois', 'Basset de Westphalie', 'Basset Hound', 'Basset Leonado de Bretaña (Basset fauve de Bretagne)', 'Bavarian Mountain Scenthound', 'Beagle', 'Beagle Harrier', 'Beauceron', 'Bedlington Terrier', 'Bichon Boloñes', 'Bichón Frisé', 'Bichón Habanero', 'Billy', 'Black and Tan Coonhound', 'Bloodhound (Sabueso de San Huberto)', 'Bobtail', 'Boerboel', 'Border Collie', 'Border terrier', 'Borzoi', 'Bosnian Hound', 'Boston terrier', 'Bouvier des Flandres', 'Boxer', 'Boyero de Appenzell', 'Boyero de Australia', 'Boyero de Entlebuch', 'Boyero de las Ardenas', 'Boyero de Montaña Bernes', 'Braco Alemán de pelo corto', 'Braco Alemán de pelo duro', 'Braco de Ariege', 'Braco de Auvernia', 'Braco de Bourbonnais', 'Braco de Saint Germain', 'Braco Dupuy', 'Braco Francés', 'Braco Italiano', 'Broholmer', 'Buhund Noruego', 'Bull terrier', 'Bulldog americano', 'Bulldog inglés', 'Bulldog francés', 'Bullmastiff', 'Ca de Bestiar', 'Cairn terrier', 'Cane Corso', 'Cane da Pastore Maremmano-Abruzzese', 'Caniche (Poodle)', 'Caniche Toy (Toy Poodle)', 'Cao da Serra de Aires', 'Cao da Serra de Estrela', 'Cao de Castro Laboreiro', 'Cao de Fila de Sao Miguel', 'Cavalier King Charles Spaniel', 'Cesky Fousek', 'Cesky Terrier', 'Chesapeake Bay Retriever', 'Chihuahua', 'Chin', 'Chow Chow', 'Cirneco del Etna', 'Clumber Spaniel', 'Cocker Spaniel Americano', 'Cocker Spaniel Inglés', 'Collie Barbudo', 'Collie de Pelo Cort', 'Collie de Pelo Largo', 'Cotón de Tuléar', 'Curly Coated Retriever', 'Dálmata', 'Dandie dinmont terrier', 'Deerhound', 'Dobermann', 'Dogo Argentino', 'Dogo de Burdeos', 'Dogo del Tibet', 'Drentse Partridge Dog', 'Drever', 'Dunker', 'Elkhound Noruego', 'Elkhound Sueco', 'English Foxhound', 'English Springer Spaniel', 'English Toy Terrier', 'Epagneul Picard', 'Eurasier', 'Fila Brasileiro', 'Finnish Lapphound', 'Flat Coated Retriever', 'Fox terrier de pelo de alambre', 'Fox terrier de pelo liso', 'Foxhound Inglés', 'Frisian Pointer', 'Galgo Español', 'Galgo húngaro (Magyar Agar)', 'Galgo Italiano', 'Galgo Polaco (Chart Polski)', 'Glen of Imaal Terrier', 'Golden Retriever', 'Gordon Setter', "Gos d'Atura Catalá", 'Gran Basset Griffon Vendeano', 'Gran Boyero Suizo', 'Gran Danés (Dogo Aleman)', 'Gran Gascón Saintongeois', 'Gran Griffon Vendeano', 'Gran Munsterlander', 'Gran Perro Japonés', 'Grand Anglo Francais Tricoleur', 'Grand Bleu de Gascogne', 'Greyhound', 'Griffon Bleu de Gascogne', 'Griffon de pelo duro (Grifón Korthals)', 'Griffon leonado de Bretaña', 'Griffon Nivernais', 'Grifon Belga', 'Grifón de Bruselas', 'Haldenstoever', 'Harrier', 'Hokkaido', 'Hovawart', 'Husky Siberiano (Siberian Husky)', 'Ioujnorousskaia Ovtcharka', 'Irish Glen of Imaal terrier', 'Irish soft coated wheaten terrier', 'Irish terrier', 'Irish Water Spaniel', 'Irish Wolfhound', 'Jack Russell terrier', 'Jindo Coreano', 'Kai', 'Keeshond', 'Kelpie australiano (Australian kelpie)', 'Kerry blue terrier', 'King Charles Spaniel', 'Kishu', 'Komondor', 'Kooiker', 'Kromfohrländer', 'Kuvasz', 'Labrador Retriever', 'Lagotto Romagnolo', 'Laika de Siberia Occidental', 'Laika de Siberia Oriental', 'Laika Ruso Europeo', 'Lakeland terrier', 'Landseer', 'Lapphund Sueco', 'Lebrel Afgano', 'Lebrel Arabe (Sloughi)', 'Leonberger', 'Lhasa Apso', 'Lowchen (Pequeño Perro León)', 'Lundehund Noruego', 'Malamute de Alaska', 'Maltés', 'Manchester terrier', 'Mastiff', 'Mastín de los Pirineos', 'Mastín Español', 'Mastín Napolitano', 'Mudi', 'Norfolk terrier', 'Norwich terrier', 'Nova Scotia duck tolling retriever', 'Ovejero alemán', 'Otterhound', 'Rafeiro do Alentejo', 'Ratonero Bodeguero Andaluz', 'Retriever de Nueva Escocia', 'Rhodesian Ridgeback', 'Ridgeback de Tailandia', 'Rottweiler', 'Saarloos', 'Sabueso de Hamilton', 'Sabueso de Hannover', 'Sabueso de Hygen', 'Sabueso de Istria', 'Sabueso de Posavaz', 'Sabueso de Schiller (Schillerstovare)', 'Sabueso de Smaland (Smalandsstovare)', 'Sabueso de Transilvania', 'Sabueso del Tirol', 'Sabueso Español', 'Sabueso Estirio de pelo duro', 'Sabueso Finlandés', 'Sabueso Francés blanco y negro', 'Sabueso Francés tricolor', 'Sabueso Griego', 'Sabueso Polaco (Ogar Polski)', 'Sabueso Serbio', 'Sabueso Suizo', 'Sabueso Yugoslavo de Montaña', 'Sabueso Yugoslavo tricolor', 'Saluki', 'Samoyedo', 'San Bernardo', 'Sarplaninac', 'Schapendoes', 'Schipperke', 'Schnauzer estándar', 'Schnauzer gigante (Riesenschnauzer)', 'Schnauzer miniatura (Zwergschnauzer)', 'Scottish terrier', 'Sealyham terrier', 'Segugio Italiano', 'Seppala Siberiano', 'Setter Inglés', 'Setter Irlandés', 'Setter Irlandés rojo y blanco', 'Shar Pei', 'Shiba Inu', 'Shih Tzu', 'Shikoku', 'Skye terrier', 'Slovensky Cuvac', 'Slovensky Kopov', 'Smoushond Holandés', 'Spaniel Alemán (German Wachtelhund)', 'Spaniel Azul de Picardía', 'Spaniel Bretón', 'Spaniel de Campo', 'Spaniel de Pont Audemer', 'Spaniel Francés', 'Spaniel Tibetano', 'Spinone Italiano', 'Spítz Alemán', 'Spitz de Norbotten (Norbottenspets)', 'Spitz Finlandés', 'Spitz Japonés', 'Staffordshire bull terrier', 'Staffordshire terrier americano', 'Sussex Spaniel', 'Teckel (Dachshund)', 'Tchuvatch eslovaco', 'Terranova (Newfoundland)', 'Terrier australiano (Australian terrier)', 'Terrier brasilero', 'Terrier cazador alemán', 'Terrier checo (Ceský teriér)', 'Terrier galés', 'Terrier irlandés (Irish terrier)', 'Terrier japonés (Nihon teria)', 'Terrier negro ruso', 'Terrier tibetano', 'Tosa', 'Viejo Pastor Inglés', 'Viejo Pointer Danés (Old Danish Pointer)', 'Vizsla', 'Volpino Italiano', 'Weimaraner', 'Welsh springer spaniel', 'Welsh Corgi Cardigan', 'Welsh Corgi Pembroke', 'Welsh terrier', 'West highland white terrier', 'Whippet', 'Wirehaired solvakian pointer', 'Xoloitzcuintle', 'Yorkshire Terrier']      
tupla = ((perro,perro) for perro in lista_perros)
class perritos(models.Model):
    nombre_perrito = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    raza = models.CharField(choices=tupla,max_length=60,default= 'Akita')
    genero = models.CharField(choices=sexo,max_length=20,default='Macho')
    tipo_casa = models.CharField(choices=tipo_casa,max_length=20,default='Departamento')
    descripcion = models.CharField(max_length=250,null=True,blank=True)
    pareja = models.ForeignKey(
            'self',  #relacion unaria
            on_delete=models.SET_NULL,  
            null=True, 
            blank=True,  
            related_name='amigo'  
        )

    def __str__(self):
        return self.nombre_perrito + " | " + self.raza
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre