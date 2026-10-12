from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    f_name = document.getElementById('fname').value.strip()
    l_name = document.getElementById('lname').value.strip()

    if not f_name or not l_name:
        display(
            'Please enter both your first and last name.',
            target='div1'
        )
        return

    full_name = f_name + ' ' + l_name

    club_members = [
        'Summer Bagiuo',
        'Keona Valdez',
        'Mariel Dieta',
        'Samantha Jose'
    ]

    name_checker = full_name.lower() in [
        name.lower() for name in club_members
    ]

    if name_checker:
        display(
            f'Congratulations, {full_name}! '
            'You are part of the Volleyball Varsity Club!',
            target='div1'
        )
    else:
        display(
            f'Sorry, {full_name}. Your name is not on the list.',
            target='div1'
        )