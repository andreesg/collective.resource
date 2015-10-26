#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.resource import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from collective.object.utils.widgets import SimpleRelatedItemsFieldWidget, AjaxSingleSelectFieldWidget
from collective.object.utils.source import ObjPathSourceBinder
from plone.directives import dexterity, form

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))

class ListField(schema.List):
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

# # # # # # # # # # # # #
# Widget interface      #
# # # # # # # # # # # # #

class IFormWidget(Interface):
    pass


# # # # # # # # # # # # # #
# DataGrid interfaces     # 
# # # # # # # # # # # # # #

# Title and author
class ITitle(Interface):
    title = schema.TextLine(title=_(u'Title'), required=False)

class ICreator(Interface):
    creator = RelationList(
        title=_(u'Creator'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('creator', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class ISubject(Interface):
    term = schema.TextLine(title=_(u'Subject'), required=False)

class IDescription(Interface):
    term = schema.TextLine(title=_(u'Description'), required=False)

class IContributor(Interface):
    contributor = RelationList(
        title=_(u'Contributor'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('contributor', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    
class IAuthor(Interface):
    author = schema.TextLine(title=_(u'Author'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IResourceType(Interface):
    term = schema.TextLine(title=_(u'Resource type'), required=False)

class IFormat(Interface):
    term = schema.TextLine(title=_(u'Format'), required=False)

class IIdentifier(Interface):
    term = schema.TextLine(title=_(u'Identifier'), required=False)

class ISource(Interface):
    term = schema.TextLine(title=_(u'Source'), required=False)

class IRelation(Interface):
    term = schema.TextLine(title=_(u'Relation'), required=False)

class ICoverage(Interface):
    term = schema.TextLine(title=_(u'Coverage'), required=False)

class IRights(Interface):
    term = schema.TextLine(title=_(u'Rights'), required=False)

class IIllustrator(Interface):
    illustrator = schema.TextLine(title=_(u'Illustrator'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IPlace(Interface):
    term =  schema.TextLine(title=_(u'Place'), required=False)

class IISSN(Interface):
    ISSN = schema.TextLine(title=_(u'ISSN'), required=False)

class IPublisher(Interface):
    publisher = RelationList(
        title=_(u'Publisher'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='PersonOrInstitution')
        ),
        required=False
    )
    form.widget('publisher', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IPlacePrinted(Interface):
    term = schema.TextLine(title=_(u'Place printed'), required=False)

class IPrinter(Interface):
    name = schema.TextLine(title=_(u'Printer'), required=False)

class IAccompanyingMaterial(Interface):
    term = schema.TextLine(title=_(u'Accompanying material'), required=False)

class IPhysicalDetails(Interface):
    term = schema.TextLine(title=_(u'Physical detail'), required=False)

class IBibliographicalNotes(Interface):
    term = schema.TextLine(title=_(u'Bibliographical notes'), required=False)

class IConference(Interface):
    term = schema.TextLine(title=_(u'Conference'), required=False)

class ISeries(Interface):
    seriesArticle = schema.TextLine(title=_(u'Series article'), required=False)
    series = schema.TextLine(title=_(u'Series'), required=False)
    seriesNo = schema.TextLine(title=_(u'Series no.'), required=False)
    ISSNSeries = schema.TextLine(title=_(u'ISSN series'), required=False)

class IIllustrations(Interface):
    term = schema.TextLine(title=_(u'Illustrations'), required=False)

class IHolding(Interface):
    term = schema.TextLine(title=_(u'Holding'), required=False)

class IContinuedFrom(Interface):
    term = schema.TextLine(title=_(u'Continued from'), required=False)

class IContinuedAs(Interface):
    term = schema.TextLine(title=_(u'Continued as'), required=False)

# Abstract and subject terms
class IMaterialType(Interface):
    term = schema.TextLine(title=_(u'Material type'), required=False)

class IBiblForm(Interface):
    term = schema.TextLine(title=_(u'Bibl. form'), required=False)

class ILanguage(Interface):
    term = schema.TextLine(title=_(u'Language'), required=False)

class INotes(Interface):
    note = schema.TextLine(title=_(u'Notes'), required=False)


class IClassNumber(Interface):
    term = schema.TextLine(title=_(u'Class number'), required=False)

class ISubjectTerm(Interface):
    subjectTermType = schema.TextLine(title=_(u'Subject term type'), required=False)
    subjectType = schema.TextLine(title=_(u'Subject term'), required=False)
    properName = schema.TextLine(title=_(u'Proper name'), required=False)

class IPersonKeywordType(Interface):
    personKeywordType = schema.TextLine(title=_(u'Person keyword type'), required=False)
    name = schema.TextLine(title=_(u'Name'), required=False)
    role = schema.TextLine(title=_(u'Role'), required=False)

class IGeographicalKeyword(Interface):
    term = schema.TextLine(title=_(u'Geographical keyword'), required=False)

class IPeriod(Interface):
    term = schema.TextLine(title=_(u'Period'), required=False)

class IDigitalReferences(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)

class IAbstract(Interface):
    term = schema.TextLine(title=_(u'Abstract'), required=False)

# Reproductions
class IReproduction(Interface):
    reference = schema.TextLine(title=_(u'Reference'), required=False)
    type = schema.TextLine(title=_(u'Type'), required=False)
    format = schema.TextLine(title=_(u'Format'), required=False)
    date = schema.TextLine(title=_(u'Date'), required=False)
    identifierURL = schema.TextLine(title=_(u'Identifier (URL)'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)

class ILinkedObjects(Interface):
    objectNumber = RelationList(
        title=_(u'Object number'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='Object')
        ),
        required=False
    )
    form.widget('objectNumber', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')


# Exhibitions, auctions, collections
class IExhibition(Interface):
    exhibitionName = RelationList(
        title=_(u'Exhibition'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            source=ObjPathSourceBinder(portal_type='Exhibition')
        ),
        required=False
    )
    form.widget('exhibitionName', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')
    notes = schema.Text(title=_(u'Notes'), required=False)


class IAuction(Interface):
    auctionName = schema.TextLine(title=_(u'Auction name'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)

class ICollection(Interface):
    collectionName = schema.TextLine(title=_(u'Collection name'), required=False)
    notes = schema.Text(title=_(u'Notes'), required=False)


# Relations
class IPartOf(Interface):
    term = schema.TextLine(title=_(u'Part of'), required=False)

class IConsistsOf(Interface):
    term = schema.TextLine(title=_(u'Consists of'), required=False)

class IMuseumObjects(Interface):
    objectNo = schema.TextLine(title=_(u'Object no.'), required=False)
    objectName = schema.TextLine(title=_(u'Object name'), required=False)
    title = schema.TextLine(title=_(u'Title'), required=False)
    maker = schema.TextLine(title=_(u'Maker'), required=False)

# Free fields
class IFreeFields(Interface):
    date = schema.TextLine(title=_(u'Date'), required=False)
    type = schema.TextLine(title=_(u'Type'), required=False)
    confidential = schema.TextLine(title=_(u'Confidential'), required=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class IOtherNumber(Interface):
    type = schema.TextLine(title=_(u'Type'), required=False)
    contents = schema.TextLine(title=_(u'Contents'), required=False)


class ICopyDetails(Interface):
    copyNumber = schema.TextLine(title=_(u'Copy number'), required=False)
    shelfMark = schema.TextLine(title=_(u'Shelf mark'), required=False)
    #availability = schema.TextLine(title=_(u'Availability'), required=False)
    loanCategory = schema.List(
        title=_(u'Loan category'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('loanCategory', AjaxSingleSelectFieldWidget, vocabulary="collective.resource.loanCategory")

    site = schema.List(
        title=_(u'Site'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('site', AjaxSingleSelectFieldWidget, vocabulary="collective.resource.site")
    locationNotes = schema.Text(title=_(u'Location notes'), required=False)

