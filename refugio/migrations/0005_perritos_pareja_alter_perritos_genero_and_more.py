# Generated by Django 4.2.5 on 2024-10-18 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refugio', '0004_perritos_tipo_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='perritos',
            name='pareja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amigo', to='refugio.perritos'),
        ),
        migrations.AlterField(
            model_name='perritos',
            name='genero',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho', max_length=20),
        ),
        migrations.AlterField(
            model_name='perritos',
            name='raza',
            field=models.CharField(choices=[('Affenpinscher', 'Affenpinscher'), ('Airedale terrier', 'Airedale terrier'), ('Akita', 'Akita'), ('Akita americano', 'Akita americano'), ('Alaskan Husky', 'Alaskan Husky'), ('Alaskan malamute', 'Alaskan malamute'), ('American Foxhound', 'American Foxhound'), ('American pit bull terrier', 'American pit bull terrier'), ('American staffordshire terrier', 'American staffordshire terrier'), ('Ariegeois', 'Ariegeois'), ('Artois', 'Artois'), ('Australian silky terrier', 'Australian silky terrier'), ('Australian Terrier', 'Australian Terrier'), ('Austrian Black & Tan Hound', 'Austrian Black & Tan Hound'), ('Azawakh', 'Azawakh'), ('Balkan Hound', 'Balkan Hound'), ('Basenji', 'Basenji'), ('Basset Alpino (Alpine Dachsbracke)', 'Basset Alpino (Alpine Dachsbracke)'), ('Basset Artesiano Normando', 'Basset Artesiano Normando'), ('Basset Azul de Gascuña (Basset Bleu de Gascogne)', 'Basset Azul de Gascuña (Basset Bleu de Gascogne)'), ('Basset de Artois', 'Basset de Artois'), ('Basset de Westphalie', 'Basset de Westphalie'), ('Basset Hound', 'Basset Hound'), ('Basset Leonado de Bretaña (Basset fauve de Bretagne)', 'Basset Leonado de Bretaña (Basset fauve de Bretagne)'), ('Bavarian Mountain Scenthound', 'Bavarian Mountain Scenthound'), ('Beagle', 'Beagle'), ('Beagle Harrier', 'Beagle Harrier'), ('Beauceron', 'Beauceron'), ('Bedlington Terrier', 'Bedlington Terrier'), ('Bichon Boloñes', 'Bichon Boloñes'), ('Bichón Frisé', 'Bichón Frisé'), ('Bichón Habanero', 'Bichón Habanero'), ('Billy', 'Billy'), ('Black and Tan Coonhound', 'Black and Tan Coonhound'), ('Bloodhound (Sabueso de San Huberto)', 'Bloodhound (Sabueso de San Huberto)'), ('Bobtail', 'Bobtail'), ('Boerboel', 'Boerboel'), ('Border Collie', 'Border Collie'), ('Border terrier', 'Border terrier'), ('Borzoi', 'Borzoi'), ('Bosnian Hound', 'Bosnian Hound'), ('Boston terrier', 'Boston terrier'), ('Bouvier des Flandres', 'Bouvier des Flandres'), ('Boxer', 'Boxer'), ('Boyero de Appenzell', 'Boyero de Appenzell'), ('Boyero de Australia', 'Boyero de Australia'), ('Boyero de Entlebuch', 'Boyero de Entlebuch'), ('Boyero de las Ardenas', 'Boyero de las Ardenas'), ('Boyero de Montaña Bernes', 'Boyero de Montaña Bernes'), ('Braco Alemán de pelo corto', 'Braco Alemán de pelo corto'), ('Braco Alemán de pelo duro', 'Braco Alemán de pelo duro'), ('Braco de Ariege', 'Braco de Ariege'), ('Braco de Auvernia', 'Braco de Auvernia'), ('Braco de Bourbonnais', 'Braco de Bourbonnais'), ('Braco de Saint Germain', 'Braco de Saint Germain'), ('Braco Dupuy', 'Braco Dupuy'), ('Braco Francés', 'Braco Francés'), ('Braco Italiano', 'Braco Italiano'), ('Broholmer', 'Broholmer'), ('Buhund Noruego', 'Buhund Noruego'), ('Bull terrier', 'Bull terrier'), ('Bulldog americano', 'Bulldog americano'), ('Bulldog inglés', 'Bulldog inglés'), ('Bulldog francés', 'Bulldog francés'), ('Bullmastiff', 'Bullmastiff'), ('Ca de Bestiar', 'Ca de Bestiar'), ('Cairn terrier', 'Cairn terrier'), ('Cane Corso', 'Cane Corso'), ('Cane da Pastore Maremmano-Abruzzese', 'Cane da Pastore Maremmano-Abruzzese'), ('Caniche (Poodle)', 'Caniche (Poodle)'), ('Caniche Toy (Toy Poodle)', 'Caniche Toy (Toy Poodle)'), ('Cao da Serra de Aires', 'Cao da Serra de Aires'), ('Cao da Serra de Estrela', 'Cao da Serra de Estrela'), ('Cao de Castro Laboreiro', 'Cao de Castro Laboreiro'), ('Cao de Fila de Sao Miguel', 'Cao de Fila de Sao Miguel'), ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'), ('Cesky Fousek', 'Cesky Fousek'), ('Cesky Terrier', 'Cesky Terrier'), ('Chesapeake Bay Retriever', 'Chesapeake Bay Retriever'), ('Chihuahua', 'Chihuahua'), ('Chin', 'Chin'), ('Chow Chow', 'Chow Chow'), ('Cirneco del Etna', 'Cirneco del Etna'), ('Clumber Spaniel', 'Clumber Spaniel'), ('Cocker Spaniel Americano', 'Cocker Spaniel Americano'), ('Cocker Spaniel Inglés', 'Cocker Spaniel Inglés'), ('Collie Barbudo', 'Collie Barbudo'), ('Collie de Pelo Cort', 'Collie de Pelo Cort'), ('Collie de Pelo Largo', 'Collie de Pelo Largo'), ('Cotón de Tuléar', 'Cotón de Tuléar'), ('Curly Coated Retriever', 'Curly Coated Retriever'), ('Dálmata', 'Dálmata'), ('Dandie dinmont terrier', 'Dandie dinmont terrier'), ('Deerhound', 'Deerhound'), ('Dobermann', 'Dobermann'), ('Dogo Argentino', 'Dogo Argentino'), ('Dogo de Burdeos', 'Dogo de Burdeos'), ('Dogo del Tibet', 'Dogo del Tibet'), ('Drentse Partridge Dog', 'Drentse Partridge Dog'), ('Drever', 'Drever'), ('Dunker', 'Dunker'), ('Elkhound Noruego', 'Elkhound Noruego'), ('Elkhound Sueco', 'Elkhound Sueco'), ('English Foxhound', 'English Foxhound'), ('English Springer Spaniel', 'English Springer Spaniel'), ('English Toy Terrier', 'English Toy Terrier'), ('Epagneul Picard', 'Epagneul Picard'), ('Eurasier', 'Eurasier'), ('Fila Brasileiro', 'Fila Brasileiro'), ('Finnish Lapphound', 'Finnish Lapphound'), ('Flat Coated Retriever', 'Flat Coated Retriever'), ('Fox terrier de pelo de alambre', 'Fox terrier de pelo de alambre'), ('Fox terrier de pelo liso', 'Fox terrier de pelo liso'), ('Foxhound Inglés', 'Foxhound Inglés'), ('Frisian Pointer', 'Frisian Pointer'), ('Galgo Español', 'Galgo Español'), ('Galgo húngaro (Magyar Agar)', 'Galgo húngaro (Magyar Agar)'), ('Galgo Italiano', 'Galgo Italiano'), ('Galgo Polaco (Chart Polski)', 'Galgo Polaco (Chart Polski)'), ('Glen of Imaal Terrier', 'Glen of Imaal Terrier'), ('Golden Retriever', 'Golden Retriever'), ('Gordon Setter', 'Gordon Setter'), ("Gos d'Atura Catalá", "Gos d'Atura Catalá"), ('Gran Basset Griffon Vendeano', 'Gran Basset Griffon Vendeano'), ('Gran Boyero Suizo', 'Gran Boyero Suizo'), ('Gran Danés (Dogo Aleman)', 'Gran Danés (Dogo Aleman)'), ('Gran Gascón Saintongeois', 'Gran Gascón Saintongeois'), ('Gran Griffon Vendeano', 'Gran Griffon Vendeano'), ('Gran Munsterlander', 'Gran Munsterlander'), ('Gran Perro Japonés', 'Gran Perro Japonés'), ('Grand Anglo Francais Tricoleur', 'Grand Anglo Francais Tricoleur'), ('Grand Bleu de Gascogne', 'Grand Bleu de Gascogne'), ('Greyhound', 'Greyhound'), ('Griffon Bleu de Gascogne', 'Griffon Bleu de Gascogne'), ('Griffon de pelo duro (Grifón Korthals)', 'Griffon de pelo duro (Grifón Korthals)'), ('Griffon leonado de Bretaña', 'Griffon leonado de Bretaña'), ('Griffon Nivernais', 'Griffon Nivernais'), ('Grifon Belga', 'Grifon Belga'), ('Grifón de Bruselas', 'Grifón de Bruselas'), ('Haldenstoever', 'Haldenstoever'), ('Harrier', 'Harrier'), ('Hokkaido', 'Hokkaido'), ('Hovawart', 'Hovawart'), ('Husky Siberiano (Siberian Husky)', 'Husky Siberiano (Siberian Husky)'), ('Ioujnorousskaia Ovtcharka', 'Ioujnorousskaia Ovtcharka'), ('Irish Glen of Imaal terrier', 'Irish Glen of Imaal terrier'), ('Irish soft coated wheaten terrier', 'Irish soft coated wheaten terrier'), ('Irish terrier', 'Irish terrier'), ('Irish Water Spaniel', 'Irish Water Spaniel'), ('Irish Wolfhound', 'Irish Wolfhound'), ('Jack Russell terrier', 'Jack Russell terrier'), ('Jindo Coreano', 'Jindo Coreano'), ('Kai', 'Kai'), ('Keeshond', 'Keeshond'), ('Kelpie australiano (Australian kelpie)', 'Kelpie australiano (Australian kelpie)'), ('Kerry blue terrier', 'Kerry blue terrier'), ('King Charles Spaniel', 'King Charles Spaniel'), ('Kishu', 'Kishu'), ('Komondor', 'Komondor'), ('Kooiker', 'Kooiker'), ('Kromfohrländer', 'Kromfohrländer'), ('Kuvasz', 'Kuvasz'), ('Labrador Retriever', 'Labrador Retriever'), ('Lagotto Romagnolo', 'Lagotto Romagnolo'), ('Laika de Siberia Occidental', 'Laika de Siberia Occidental'), ('Laika de Siberia Oriental', 'Laika de Siberia Oriental'), ('Laika Ruso Europeo', 'Laika Ruso Europeo'), ('Lakeland terrier', 'Lakeland terrier'), ('Landseer', 'Landseer'), ('Lapphund Sueco', 'Lapphund Sueco'), ('Lebrel Afgano', 'Lebrel Afgano'), ('Lebrel Arabe (Sloughi)', 'Lebrel Arabe (Sloughi)'), ('Leonberger', 'Leonberger'), ('Lhasa Apso', 'Lhasa Apso'), ('Lowchen (Pequeño Perro León)', 'Lowchen (Pequeño Perro León)'), ('Lundehund Noruego', 'Lundehund Noruego'), ('Malamute de Alaska', 'Malamute de Alaska'), ('Maltés', 'Maltés'), ('Manchester terrier', 'Manchester terrier'), ('Mastiff', 'Mastiff'), ('Mastín de los Pirineos', 'Mastín de los Pirineos'), ('Mastín Español', 'Mastín Español'), ('Mastín Napolitano', 'Mastín Napolitano'), ('Mudi', 'Mudi'), ('Norfolk terrier', 'Norfolk terrier'), ('Norwich terrier', 'Norwich terrier'), ('Nova Scotia duck tolling retriever', 'Nova Scotia duck tolling retriever'), ('Ovejero alemán', 'Ovejero alemán'), ('Otterhound', 'Otterhound'), ('Rafeiro do Alentejo', 'Rafeiro do Alentejo'), ('Ratonero Bodeguero Andaluz', 'Ratonero Bodeguero Andaluz'), ('Retriever de Nueva Escocia', 'Retriever de Nueva Escocia'), ('Rhodesian Ridgeback', 'Rhodesian Ridgeback'), ('Ridgeback de Tailandia', 'Ridgeback de Tailandia'), ('Rottweiler', 'Rottweiler'), ('Saarloos', 'Saarloos'), ('Sabueso de Hamilton', 'Sabueso de Hamilton'), ('Sabueso de Hannover', 'Sabueso de Hannover'), ('Sabueso de Hygen', 'Sabueso de Hygen'), ('Sabueso de Istria', 'Sabueso de Istria'), ('Sabueso de Posavaz', 'Sabueso de Posavaz'), ('Sabueso de Schiller (Schillerstovare)', 'Sabueso de Schiller (Schillerstovare)'), ('Sabueso de Smaland (Smalandsstovare)', 'Sabueso de Smaland (Smalandsstovare)'), ('Sabueso de Transilvania', 'Sabueso de Transilvania'), ('Sabueso del Tirol', 'Sabueso del Tirol'), ('Sabueso Español', 'Sabueso Español'), ('Sabueso Estirio de pelo duro', 'Sabueso Estirio de pelo duro'), ('Sabueso Finlandés', 'Sabueso Finlandés'), ('Sabueso Francés blanco y negro', 'Sabueso Francés blanco y negro'), ('Sabueso Francés tricolor', 'Sabueso Francés tricolor'), ('Sabueso Griego', 'Sabueso Griego'), ('Sabueso Polaco (Ogar Polski)', 'Sabueso Polaco (Ogar Polski)'), ('Sabueso Serbio', 'Sabueso Serbio'), ('Sabueso Suizo', 'Sabueso Suizo'), ('Sabueso Yugoslavo de Montaña', 'Sabueso Yugoslavo de Montaña'), ('Sabueso Yugoslavo tricolor', 'Sabueso Yugoslavo tricolor'), ('Saluki', 'Saluki'), ('Samoyedo', 'Samoyedo'), ('San Bernardo', 'San Bernardo'), ('Sarplaninac', 'Sarplaninac'), ('Schapendoes', 'Schapendoes'), ('Schipperke', 'Schipperke'), ('Schnauzer estándar', 'Schnauzer estándar'), ('Schnauzer gigante (Riesenschnauzer)', 'Schnauzer gigante (Riesenschnauzer)'), ('Schnauzer miniatura (Zwergschnauzer)', 'Schnauzer miniatura (Zwergschnauzer)'), ('Scottish terrier', 'Scottish terrier'), ('Sealyham terrier', 'Sealyham terrier'), ('Segugio Italiano', 'Segugio Italiano'), ('Seppala Siberiano', 'Seppala Siberiano'), ('Setter Inglés', 'Setter Inglés'), ('Setter Irlandés', 'Setter Irlandés'), ('Setter Irlandés rojo y blanco', 'Setter Irlandés rojo y blanco'), ('Shar Pei', 'Shar Pei'), ('Shiba Inu', 'Shiba Inu'), ('Shih Tzu', 'Shih Tzu'), ('Shikoku', 'Shikoku'), ('Skye terrier', 'Skye terrier'), ('Slovensky Cuvac', 'Slovensky Cuvac'), ('Slovensky Kopov', 'Slovensky Kopov'), ('Smoushond Holandés', 'Smoushond Holandés'), ('Spaniel Alemán (German Wachtelhund)', 'Spaniel Alemán (German Wachtelhund)'), ('Spaniel Azul de Picardía', 'Spaniel Azul de Picardía'), ('Spaniel Bretón', 'Spaniel Bretón'), ('Spaniel de Campo', 'Spaniel de Campo'), ('Spaniel de Pont Audemer', 'Spaniel de Pont Audemer'), ('Spaniel Francés', 'Spaniel Francés'), ('Spaniel Tibetano', 'Spaniel Tibetano'), ('Spinone Italiano', 'Spinone Italiano'), ('Spítz Alemán', 'Spítz Alemán'), ('Spitz de Norbotten (Norbottenspets)', 'Spitz de Norbotten (Norbottenspets)'), ('Spitz Finlandés', 'Spitz Finlandés'), ('Spitz Japonés', 'Spitz Japonés'), ('Staffordshire bull terrier', 'Staffordshire bull terrier'), ('Staffordshire terrier americano', 'Staffordshire terrier americano'), ('Sussex Spaniel', 'Sussex Spaniel'), ('Teckel (Dachshund)', 'Teckel (Dachshund)'), ('Tchuvatch eslovaco', 'Tchuvatch eslovaco'), ('Terranova (Newfoundland)', 'Terranova (Newfoundland)'), ('Terrier australiano (Australian terrier)', 'Terrier australiano (Australian terrier)'), ('Terrier brasilero', 'Terrier brasilero'), ('Terrier cazador alemán', 'Terrier cazador alemán'), ('Terrier checo (Ceský teriér)', 'Terrier checo (Ceský teriér)'), ('Terrier galés', 'Terrier galés'), ('Terrier irlandés (Irish terrier)', 'Terrier irlandés (Irish terrier)'), ('Terrier japonés (Nihon teria)', 'Terrier japonés (Nihon teria)'), ('Terrier negro ruso', 'Terrier negro ruso'), ('Terrier tibetano', 'Terrier tibetano'), ('Tosa', 'Tosa'), ('Viejo Pastor Inglés', 'Viejo Pastor Inglés'), ('Viejo Pointer Danés (Old Danish Pointer)', 'Viejo Pointer Danés (Old Danish Pointer)'), ('Vizsla', 'Vizsla'), ('Volpino Italiano', 'Volpino Italiano'), ('Weimaraner', 'Weimaraner'), ('Welsh springer spaniel', 'Welsh springer spaniel'), ('Welsh Corgi Cardigan', 'Welsh Corgi Cardigan'), ('Welsh Corgi Pembroke', 'Welsh Corgi Pembroke'), ('Welsh terrier', 'Welsh terrier'), ('West highland white terrier', 'West highland white terrier'), ('Whippet', 'Whippet'), ('Wirehaired solvakian pointer', 'Wirehaired solvakian pointer'), ('Xoloitzcuintle', 'Xoloitzcuintle'), ('Yorkshire Terrier', 'Yorkshire Terrier')], default='Akita', max_length=60),
        ),
    ]
