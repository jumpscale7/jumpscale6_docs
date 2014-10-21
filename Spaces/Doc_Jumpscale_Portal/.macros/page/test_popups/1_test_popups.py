from JumpScale.portal.docgenerator.popup import Popup

def main(j, args, params, tags, tasklet):
    params.result = page = args.page


    popup = Popup(id="popup_id", header='Text popup', submit_url='aaa')
    popup.addText('First name', 'firstname', required=True)
    popup.addNumber('Age', 'age')
    popup.addDropdown('Choose licence', 'license', [('MIT', 'mit'), ('BSD', 'bsd'), ('GPL version 3', 'gpl3')])
    popup.addRadio('Choose licence', 'license2', [('MIT', 'mit'), ('BSD', 'bsd'), ('GPL version 3', 'gpl3')])
    popup.addCheckboxes('Choose the software', 'software', [('MS Office', 'msoffice'), ('Photoshop', 'photoshop')])
    page.addMessage(popup.to_html())

    return params


def match(j, args, params, tags, tasklet):
    return True
