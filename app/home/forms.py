from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, SelectField
from wtforms.validators import Required,Email,EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Category

class CategoryForm(FlaskForm):
    category_name = StringField('Add a new category',validators=[Required()])
    submit = SubmitField('Add Category')


class PitchForm(FlaskForm):
    pitch_title = StringField('Add a pitch title',validators=[Required()])
    pitch_content = StringField('Add a pitch',validators=[Required()])
    category_name = QuerySelectField(query_factory= lambda: Category.query.all())
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    comment_content = StringField('Add a comment',validators=[Required()])
    submit = SubmitField('Add Comment')
