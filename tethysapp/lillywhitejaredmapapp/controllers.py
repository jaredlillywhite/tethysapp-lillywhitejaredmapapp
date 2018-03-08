from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, RangeSlider, ToggleSwitch, MessageBox, ButtonGroup

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'lillywhitejaredmapapp/home.html', context)

def mapview(request):
    grade_slider = RangeSlider(display_text='Desired Average Grade',
                               name='grade_slider',
                               min=0,
                               max = .1,
                               initial = .05,
                               step = .01)


    find_route_button = Button(display_text = 'Calculate Route',
                               icon = 'glyphicon',
                               style = 'success')

    frontrunner_toggle_switch = ToggleSwitch(display_text='Frontrunner Stations', name='toggle1')
    dem_toggle_switch = ToggleSwitch(display_text='Utah DEM', name='toggle4')
    starting_point_button = Button(display_text='Add Starting Location',
                                   icon='glyphicon glyphicon-plus',
                                   style='success')
    ending_point_button = Button(display_text='Add Ending Location',
                                 icon='glyphicon glyphicon-plus',
                                 style='success')
    vertical_buttons = ButtonGroup(buttons=[starting_point_button, ending_point_button], vertical=True)


    context = {'grade_slider': grade_slider,
               'frontrunner_toggle_switch': frontrunner_toggle_switch,
               'dem_toggle_switch': dem_toggle_switch,
               'vertical_buttons': vertical_buttons,
               'find_route_button': find_route_button,
               }



    return render(request,'lillywhitejaredmapapp/MapView.html', context)

def dataservices(request):
    context = {

    }

    return render(request, 'lillywhitejaredmapapp/dataservices.html', context)

def about(request):

    message_box = MessageBox(name='sampleModal',
                             title='About Me',
                             message="I am a Civil Engineering student posing as a web app developer. I enjoy rooting for teams that always lose, such as the Utah Jazz, the BYU Cougars, and independent political candidates. The only winner I've ever picked in my life is my beautiful wife of 2 years. Hope you liked my app.",
                             width=400,
                             affirmative_attributes='href=javascript:void(0);')
    context = {
        'message_box': message_box,
    }

    return render(request,'lillywhitejaredmapapp/about.html',context)

def proposal(request):
    context = {

    }

    return render(request,'lillywhitejaredmapapp/proposal.html', context)

def mockup(request):
    context = {

    }

    return render(request, 'lillywhitejaredmapapp/mockup.html')