from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class RequestForm(forms.Form):
    name = forms.CharField(label='Your Email', max_length=200, required=True)
    dest = forms.CharField(label='Destination', max_length=100, required=True)
    arrival = forms.ChoiceField(label='Arrival Window',
                              choices=( ("1:00am-2:00am", "1:00am-2:00am"),
                                        ("2:00am-3:00am", "2:00am-3:00am"),
                                        ("3:00am-4:00am", "3:00am-4:00am"),
                                        ("4:00am-5:00am", "4:00am-5:00am"),
                                        ("5:00am-6:00am", "5:00am-6:00am"),
                                        ("6:00am-7:00am", "6:00am-7:00am"),
                                        ("7:00am-8:00am", "7:00am-8:00am"),
                                        ("8:00am-9:00am", "8:00am-9:00am"),
                                        ("9:00am-10:00am", "9:00am-10:00am"),
                                        ("10:00am-11:00am", "10:00am-11:00am"),
                                        ("11:00am-12:00pm", "11:00am-12:00pm"),
                                        ("1:00pm-2:00pm", "1:00pm-2:00pm"),
                                        ("2:00pm-3:00pm", "2:00pm-3:00pm"),
                                        ("3:00pm-4:00pm", "3:00pm-4:00pm"),
                                        ("4:00pm-5:00pm", "4:00pm-5:00pm"),
                                        ("5:00pm-6:00pm", "5:00pm-6:00pm"),
                                        ("6:00pm-7:00pm", "6:00pm-7:00pm"),
                                        ("7:00pm-8:00pm", "7:00pm-8:00pm"),
                                        ("8:00pm-9:00pm", "8:00pm-9:00pm"),
                                        ("9:00pm-10:00pm", "9:00pm-10:00pm"),
                                        ("10:00pm-11:00pm", "10:00pm-11:00pm"),
                                        ("11:00pm-12:00am", "11:00pm-12:00am")
                                        ))
    pnum = forms.IntegerField(label='Number of Passengers', required=True, validators=[MinValueValidator(1), MaxValueValidator(7)])
    vtype = forms.ChoiceField(label='Vehicle Type',
                              choices=( ("Sedan", "Sedan"),
                                        ("SUV", "SUV")))
    child = forms.BooleanField(label='Child Seat(optional)', required=False)
    share = forms.BooleanField(required=False)
    
class SharedForm(forms.Form):
    name = forms.CharField(label='Your Email', max_length=200, required=True)
    dest = forms.CharField(label='Destination', max_length=100, required=True)
    arrival = forms.ChoiceField(label='Arrival Window',
                              choices=( ("1:00am-2:00am", "1:00am-2:00am"),
                                        ("2:00am-3:00am", "2:00am-3:00am"),
                                        ("3:00am-4:00am", "3:00am-4:00am"),
                                        ("4:00am-5:00am", "4:00am-5:00am"),
                                        ("5:00am-6:00am", "5:00am-6:00am"),
                                        ("6:00am-7:00am", "6:00am-7:00am"),
                                        ("7:00am-8:00am", "7:00am-8:00am"),
                                        ("8:00am-9:00am", "8:00am-9:00am"),
                                        ("9:00am-10:00am", "9:00am-10:00am"),
                                        ("10:00am-11:00am", "10:00am-11:00am"),
                                        ("11:00am-12:00pm", "11:00am-12:00pm"),
                                        ("1:00pm-2:00pm", "1:00pm-2:00pm"),
                                        ("2:00pm-3:00pm", "2:00pm-3:00pm"),
                                        ("3:00pm-4:00pm", "3:00pm-4:00pm"),
                                        ("4:00pm-5:00pm", "4:00pm-5:00pm"),
                                        ("5:00pm-6:00pm", "5:00pm-6:00pm"),
                                        ("6:00pm-7:00pm", "6:00pm-7:00pm"),
                                        ("7:00pm-8:00pm", "7:00pm-8:00pm"),
                                        ("8:00pm-9:00pm", "8:00pm-9:00pm"),
                                        ("9:00pm-10:00pm", "9:00pm-10:00pm"),
                                        ("10:00pm-11:00pm", "10:00pm-11:00pm"),
                                        ("11:00pm-12:00am", "11:00pm-12:00am")
                                        ))
    pnum = forms.IntegerField(label='Number of Passengers', required=True, validators=[MinValueValidator(1), MaxValueValidator(7)])

    


