import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

class Open56Block(XBlock):
    """
    An XBlock providing Open56 capabilities for video
    """

    src = String(help="URL of the video page at the provider", default=None, scope=Scope.content)
    width = Integer(help="width of the video", default=800, scope=Scope.content)
    height = Integer(help="height of the video", default=450, scope=Scope.content)

    def student_view(self, context=None):
        """
        The primary view of the Open56Block, shown to students
        when viewing courses.
        """
        # Load the HTML fragment from within the package and fill in the template
        html_str = pkg_resources.resource_string(__name__, "static/html/open56_view.html")
        frag = Fragment(unicode(html_str).format(src=self.src, width=self.width, height=self.height))
        # Load CSS
        css_str = pkg_resources.resource_string(__name__, "static/css/open56.css")
        frag.add_css(unicode(css_str))
        return frag

    def studio_view(self, context):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        html_str = pkg_resources.resource_string(__name__, "static/html/open56_edit.html")
        src = self.src or ''
        frag = Fragment(unicode(html_str).format(src=src, width=self.width, height=self.height))

        js_str = pkg_resources.resource_string(__name__, "static/js/src/open56_edit.js")
        frag.add_javascript(unicode(js_str))
        frag.initialize_js('Open56EditBlock')

        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.src = data.get('src')
        self.width = data.get('width')
        self.height = data.get('height')

        return {'result': 'success'}

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Open 56",
            """
            <vertical_demo>
                <open56 src="http://v.56.com/open_iframeplayer/3000005311_NjQzNTcxMDA.html" width="800" height="450" />
                <html_demo><div>Rate the video:</div></html_demo>
                <thumbs />
            </vertical_demo>
            """)
        ]
