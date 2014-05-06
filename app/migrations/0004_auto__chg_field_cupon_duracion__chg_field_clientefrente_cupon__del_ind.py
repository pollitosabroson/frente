# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Cupon.duracion'
        db.alter_column(u'app_cupon', 'duracion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Renaming column for 'ClienteFrente.cupon' to match new field type.
        db.rename_column(u'app_clientefrente', 'cupon_id', 'cupon')
        # Changing field 'ClienteFrente.cupon'
        db.alter_column(u'app_clientefrente', 'cupon', self.gf('django.db.models.fields.CharField')(max_length=4, null=True))
        # Removing index on 'ClienteFrente', fields ['cupon']
        db.delete_index(u'app_clientefrente', ['cupon_id'])


    def backwards(self, orm):
        # Adding index on 'ClienteFrente', fields ['cupon']
        db.create_index(u'app_clientefrente', ['cupon_id'])


        # Changing field 'Cupon.duracion'
        db.alter_column(u'app_cupon', 'duracion', self.gf('django.db.models.fields.CharField')(default=0, max_length=50))

        # Renaming column for 'ClienteFrente.cupon' to match new field type.
        db.rename_column(u'app_clientefrente', 'cupon', 'cupon_id')
        # Changing field 'ClienteFrente.cupon'
        db.alter_column(u'app_clientefrente', 'cupon_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Cupon'], null=True))

    models = {
        u'app.canal_distribucion': {
            'Meta': {'object_name': 'Canal_distribucion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_Distribucion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_Categoria': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellido_Materno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellido_Paterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '10'})
        },
        u'app.clientefrente': {
            'Colonia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Colonia_frente']"}),
            'Meta': {'object_name': 'ClienteFrente'},
            'apellido_Materno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'apellido_Paterno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categoria']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cumpleanos': ('django.db.models.fields.DateField', [], {}),
            'cupon': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Delegacion_frente']"}),
            'entregas': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_Exterior': ('django.db.models.fields.IntegerField', [], {'max_length': '10000'}),
            'numero_Interior': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rutas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Ruta']", 'null': 'True', 'symmetrical': 'False'}),
            'subcategoria1': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria1']", 'null': 'True'}),
            'subcategoria2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria2']", 'null': 'True'}),
            'subcategoria3': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria3']", 'null': 'True'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'app.colonia': {
            'Meta': {'object_name': 'Colonia'},
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Delegacion']"}),
            'descripcion_Colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.colonia_frente': {
            'Meta': {'object_name': 'Colonia_frente'},
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Delegacion_frente']"}),
            'descripcion_Colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cupon': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fechafinal': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuariogen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.cuponera': {
            'Meta': {'object_name': 'Cuponera'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cliente']"}),
            'cupon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cupon']"}),
            'fechafinal': ('django.db.models.fields.DateField', [], {}),
            'fechainicio': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.delegacion': {
            'Meta': {'object_name': 'Delegacion'},
            'descripcion_Delegacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.delegacion_frente': {
            'Meta': {'object_name': 'Delegacion_frente'},
            'descripcion_Delegacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.empresa': {
            'Colonia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Colonia']"}),
            'Meta': {'object_name': 'Empresa'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categoria']", 'null': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Cliente']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Delegacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreEmpresa': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_Exterior': ('django.db.models.fields.IntegerField', [], {}),
            'numero_Interior': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'position': ('geoposition.fields.GeopositionField', [], {'default': "'0,0'", 'max_length': '42', 'null': 'True'}),
            'rutas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Ruta']", 'symmetrical': 'False'}),
            'subcategoria1': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria1']", 'null': 'True'}),
            'subcategoria2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria2']", 'null': 'True'}),
            'subcategoria3': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Subcategoria3']", 'null': 'True'})
        },
        u'app.repartidor': {
            'Meta': {'object_name': 'Repartidor'},
            'apellido_Materno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellido_Paterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rutas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Ruta']", 'symmetrical': 'False'})
        },
        u'app.ruta': {
            'Meta': {'object_name': 'Ruta'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_Ruta': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_Ruta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.subcategoria1': {
            'Meta': {'object_name': 'Subcategoria1'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_SubCategoria1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.subcategoria2': {
            'Meta': {'object_name': 'Subcategoria2'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_SubCategoria2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.subcategoria3': {
            'Meta': {'object_name': 'Subcategoria3'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion_SubCategoria3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']