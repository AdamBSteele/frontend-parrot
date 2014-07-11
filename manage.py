from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, DateField, DateTimeField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import Required


MONTHS = [('Jan', 'JANUARY'), ('Feb', 'FEBRUARY'), ('dwt', 'DEALWITHIT.JPG')]
class EchoForm(Form):
    Status = StringField(u'Echo', widget=TextArea())
    submit_button = SubmitField('Submit Form')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

class SquawkForm(Form):
    Status = StringField(u'Squawk', widget=TextArea())
    startMonth = SelectField(u'Start Month', choices=MONTHS)
    submit_button = SubmitField('Submit Form')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

class CampaignForm(Form):
    Status = StringField(u'Campaign', widget=TextArea())
    startTime = DateField(u'Start Date/Time')
    endTime = DateTimeField(u'End Date/Time')
    endMonth = SelectField(u'end month', choices=MONTHS)
    submit_button = SubmitField('Create Campaign')



    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/timedTweet/')
    def echo():
        form = EchoForm()
        form.validate_on_submit() #to get error messages to the browser
        return render_template('timedTweet.html', form=form)

    @app.route('/keepAlive/')
    def squawk():
        form = SquawkForm()
        form.validate_on_submit() #to get error messages to the browser
        return render_template('keepAlive.html', form=form)

    @app.route('/campaign/')
    def campaign():
        form = CampaignForm()
        form.validate_on_submit() #to get error messages to the browser
        return render_template('campaign.html', form=form)

    return app

create_app().run(debug=True)