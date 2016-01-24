#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
from datetime import datetime

db.define_table(
    'gaighlig',
    # For all entries:
    Field('english', label = 'English', required = True),
    Field('sense', label = 'Sense', default = '<none>'),
    Field('gaelic', label = 'Gaelic', required = True),
    Field('pos', label = 'Part of speech', required = True),
    Field('pos_extra', label = 'Part of speech detailed', default = '<none>'),
    Field('post_asp', 'boolean', label = 'Post-aspiration', default = False),
                    
    # Nouns
    Field('gender', label = 'Gender'),
    Field('nom_sg_def', label = 'Nomininative singular definite'),
    Field('gen_sg', label = 'Genetive singular'),
    Field('dat_sg', label = 'Dative singular', default = '<none>'),
    Field('nom_pl', label = 'Nominative plural'),
    Field('gen_pl', label = 'Genetive plural', default = '<none>'),

    # Vs
    Field('second_sg_imperative', label = 'Second singular imperative'),
    Field('v_noun', label = 'Verbal noun'),
    
    # Adjs
    Field('comp', label = 'Comparative'),
    
    # Advs
    
    # Preps
    Field('n_case', label = 'Noun case'),
    
    # Expressions
    Field('lit', label = 'Literal', default = '<none>'),
    
    # Expressions w/in entries
    Field('expressions', label = 'Expressions', default = '<none>'),

    # Other stuff
    Field('created_on', default = datetime.utcnow()),
    Field('created_by', default = 'DSP')
    
)
