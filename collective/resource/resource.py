#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Zope dependencies
#
from zope import schema
from zope.interface import invariant, Invalid, Interface, implements
from zope.interface import alsoProvides
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.fieldproperty import FieldProperty
from zope.component import getMultiAdapter

#
# Plone dependencies
#
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.content.interfaces import INameFromTitle

#
# z3c.forms dependencies
#
from z3c.form import group, field
from z3c.form.form import extends
from z3c.form.browser.textlines import TextLinesFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
#from plone.formwidget.contenttree import ObjPathSourceBinder

#from .utils.source import ObjPathSourceBinder

#
# plone.app.widgets dependencies
#
from plone.app.widgets.dx import DatetimeFieldWidget, RelatedItemsFieldWidget

#
# DataGridFields dependencies
#
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridFieldFactory

# # # # # # # # # # # # # # # 
# Dexterity imports         # 
# # # # # # # # # # # # # # # 
from five import grok
from collective import dexteritytextindexer
from plone.dexterity.browser.view import DefaultView
from plone.dexterity.content import Container
from plone.dexterity.browser import add, edit
from plone.app.widgets.dx import AjaxSelectFieldWidget

# # # # # # # # # # # # # # # # # #
# !Resource specific imports!     #
# # # # # # # # # # # # # # # # # #
from collective.resource import MessageFactory as _
from .utils.vocabularies import *
from .utils.interfaces import *
from .utils.views import *

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from collective.object.utils.widgets import SimpleRelatedItemsFieldWidget, AjaxSingleSelectFieldWidget, ExtendedRelatedItemsFieldWidget
from collective.object.utils.source import ObjPathSourceBinder
from plone.directives import dexterity, form
from collective.z3cform.datagridfield.interfaces import IDataGridField

from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from Acquisition import aq_inner
from zc.relation.interfaces import ICatalog

# # # # # # # # # # # # ###
# # # # # # # # # # # # ###
# Resource schema         #
# # # # # # # # # # # # ###
# # # # # # # # # # # # ###


class INameFromPersonNames(INameFromTitle):
    def title():
        """Return a processed title"""

class NameFromPersonNames(object):
    implements(INameFromPersonNames)
    
    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return self.context.resourceDublinCore_title[0]['title']

class IResource(form.Schema):

    priref = schema.TextLine(
        title=_(u'priref'),
        required=False
    )
    dexteritytextindexer.searchable('priref')

    text = RichText(
        title=_(u"Body"),
        required=False
    )

    # # # # # # # # # # # # # # # # # # # # # # # #
    # Resource (Dublin Core)                      #
    # # # # # # # # # # # # # # # # # # # # # # # #
    model.fieldset('resource_dublin_core', label=_(u'Resource (Dublin Core)'), 
        fields=['resourceDublinCore_title', 'resourceDublinCore_creators',
        'resourceDublinCore_subject', 'resourceDublinCore_description',
        'resourceDublinCore_publishers', 'resourceDublinCore_contributors',
        'resourceDublinCore_date', 'resourceDublinCore_resourceType',
        'resourceDublinCore_format', 'resourceDublinCore_identifier',
        'resourceDublinCore_sortYear_sortYear', 'resourceDublinCore_source',
        'resourceDublinCore_language', 'resourceDublinCore_relation',
        'resourceDublinCore_coverage', 'resourceDublinCore_rights']
    )

    resourceDublinCore_title = ListField(title=_(u'Reproduction'),
        value_type=DictRow(title=_(u'Reproduction'), schema=ITitle),
        required=True)
    form.widget(resourceDublinCore_title=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_title')

    resourceDublinCore_creators = RelationList(
        title=_(u'Creator'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('resourceDublinCore_creators', ExtendedRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    
    resourceDublinCore_subject = schema.List(
        title=_(u'Subject'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('resourceDublinCore_subject', AjaxSelectFieldWidget, vocabulary="collective.resource.subject")
    
    resourceDublinCore_description = ListField(title=_(u'Description'),
        value_type=DictRow(title=_(u'Description'), schema=IDescription),
        required=False)
    form.widget(resourceDublinCore_description=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_description')
    
    resourceDublinCore_publishers = RelationList(
        title=_(u'Publisher'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('resourceDublinCore_publishers', ExtendedRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    
    resourceDublinCore_contributors = RelationList(
        title=_(u'Contributor'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('resourceDublinCore_contributors', ExtendedRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    
    resourceDublinCore_date = schema.TextLine(
        title=_(u'Date'),
        required=False
    )
    dexteritytextindexer.searchable('resourceDublinCore_date')
    
    resourceDublinCore_resourceType = schema.List(
        title=_(u'Resource type'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('resourceDublinCore_resourceType', AjaxSelectFieldWidget, vocabulary="collective.resource.resourceType")

    resourceDublinCore_format = ListField(title=_(u'Format'),
        value_type=DictRow(title=_(u'Format'), schema=IFormat),
        required=False)
    form.widget(resourceDublinCore_format=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_format')

    resourceDublinCore_identifier = ListField(title=_(u'Identifier'),
        value_type=DictRow(title=_(u'Identifier'), schema=IIdentifier),
        required=False)
    form.widget(resourceDublinCore_identifier=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_identifier')

    # Sort year
    resourceDublinCore_sortYear_sortYear = schema.TextLine(
        title=_(u'Sort year'),
        required=False
    )
    dexteritytextindexer.searchable('resourceDublinCore_sortYear_sortYear')

    resourceDublinCore_source = ListField(title=_(u'Source'),
        value_type=DictRow(title=_(u'Source'), schema=ISource),
        required=False)
    form.widget(resourceDublinCore_source=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_source')
    
    resourceDublinCore_language = schema.List(
        title=_(u'Language'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('resourceDublinCore_language', AjaxSelectFieldWidget, vocabulary="collective.resource.language")


    resourceDublinCore_relation = ListField(title=_(u'Relation'),
        value_type=DictRow(title=_(u'Relation'), schema=IRelation),
        required=False)
    form.widget(resourceDublinCore_relation=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_relation')
    
    resourceDublinCore_coverage = ListField(title=_(u'Coverage'),
        value_type=DictRow(title=_(u'Coverage'), schema=ICoverage),
        required=False)
    form.widget(resourceDublinCore_coverage=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_coverage')
    
    resourceDublinCore_rights = ListField(title=_(u'Rights'),
        value_type=DictRow(title=_(u'Rights'), schema=IRights),
        required=False)
    form.widget(resourceDublinCore_rights=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('resourceDublinCore_rights')


    # # # # # # # # # #
    # Reproductions   #
    # # # # # # # # # #
    model.fieldset('reproductions', label=_(u'Reproductions'), 
        fields=['reproductions_reproduction']
    )

    # Reproduction
    reproductions_reproduction = ListField(title=_(u'Reproduction'),
        value_type=DictRow(title=_(u'Reproduction'), schema=IReproduction),
        required=False)
    form.widget(reproductions_reproduction=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('reproductions_reproduction')


    # # # # # # # # # # # # # # # # # # # # #
    # Exhibitions, auctions, collections    #
    # # # # # # # # # # # # # # # # # # # # #
    model.fieldset('exhibitions_auctions_collections', label=_(u'Exhibitions, auctions, collections'), 
        fields=['exhibitionsAuctionsCollections_exhibition', 'exhibitionsAuctionsCollections_auction',
                'exhibitionsAuctionsCollections_collection']
    )

    # Exhibition
    exhibitionsAuctionsCollections_exhibition = ListField(title=_(u'Exhibition'),
        value_type=DictRow(title=_(u'Exhibition'), schema=IExhibition),
        required=False)
    form.widget(exhibitionsAuctionsCollections_exhibition=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('exhibitionsAuctionsCollections_exhibition')

    # Auction
    exhibitionsAuctionsCollections_auction = ListField(title=_(u'Auction'),
        value_type=DictRow(title=_(u'Auction'), schema=IAuction),
        required=False)
    form.widget(exhibitionsAuctionsCollections_auction=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('exhibitionsAuctionsCollections_auction')

    # Collection
    exhibitionsAuctionsCollections_collection = ListField(title=_(u'Collection'),
        value_type=DictRow(title=_(u'Collection'), schema=ICollection),
        required=False)
    form.widget(exhibitionsAuctionsCollections_collection=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('exhibitionsAuctionsCollections_collection')


    # # # # # # # # # # #
    # Linked objects    #
    # # # # # # # # # # #

    model.fieldset('linked_objects', label=_(u'Linked Objects'), 
        fields=[]
    )
    """
    linkedObjects_linkedobjects = RelationList(
        title=_(u'Contributor'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='Object')
        ),
        required=False
    )
    form.widget('linkedObjects_linkedobjects', ExtendedRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')"""



    # # # # # # # # # # # # # # # # # # # # #
    # Copies and shelf marks                #
    # # # # # # # # # # # # # # # # # # # # # 

    model.fieldset('copies_and_shelf_marks', label=_(u'Copies and shelf marks'), 
        fields=['copiesAndShelfMarks_defaultShelfMark', 'copiesAndShelfMarks_copyDetails']
    )

    copiesAndShelfMarks_defaultShelfMark = schema.TextLine(
        title=_(u'Default shelf mark'),
        required=False
    )
    dexteritytextindexer.searchable('copiesAndShelfMarks_defaultShelfMark')

    # Copy details
    copiesAndShelfMarks_copyDetails = ListField(title=_(u'Copy details'),
        value_type=DictRow(title=_(u'Copy details'), schema=ICopyDetails),
        required=False)
    form.widget(copiesAndShelfMarks_copyDetails=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('copiesAndShelfMarks_copyDetails')



# # # # # # # # # # # # # # #
# Resource declaration      #
# # # # # # # # # # # # # # #

class Resource(Container):
    grok.implements(IResource)

    def Title(self):
        ''' Return a title from title author '''
        try:
            return self.resourceDublinCore_title[0]['title']
        except:
            return ""

    @property
    def title(self):
        ''' return title '''
        return self.resourceDublinCore_title[0]['title']

    @title.setter
    def title(self, value):
        try:
            self.resourceDublinCore_title[0]['title'] = value
        except:
            pass


# # # # # # # # # # # # # #
# Resource add/edit views # 
# # # # # # # # # # # # # #

class AddForm(add.DefaultAddForm):
    template = ViewPageTemplateFile('resource_templates/add.pt')
    def update(self):
        super(AddForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                alsoProvides(widget, IFormWidget)    

    def getRelatedObjects(self):
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context

        relations = catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                from_attribute="documentation_documentation")
        )

        structure = ""
        for rel in list(relations):
            from_object = rel.from_object
            title = getattr(from_object, 'title', '')
            obj_number = getattr(from_object, 'identification_identification_objectNumber', '')
            url = from_object.absolute_url()
            structure += "<p><a href='%s'><span>%s</span> - <span>%s</span></a></p>" %(url, obj_number, title)

        return structure    

class AddView(add.DefaultAddView):
    form = AddForm
    

class EditForm(edit.DefaultEditForm):
    template = ViewPageTemplateFile('resource_templates/edit.pt')

    def getRelatedObjects(self):
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context

        relations = catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                from_attribute="documentation_documentation")
        )

        structure = ""
        for rel in list(relations):
            from_object = rel.from_object
            title = getattr(from_object, 'title', '')
            obj_number = getattr(from_object, 'identification_identification_objectNumber', '')
            url = from_object.absolute_url()
            structure += "<p><a href='%s'><span>%s</span> - <span>%s</span></a></p>" %(url, obj_number, title)

        return structure
    
    def update(self):
        super(EditForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                if IDataGridField.providedBy(widget):
                    widget.auto_append = False
                    widget.allow_reorder = True
                alsoProvides(widget, IFormWidget)





