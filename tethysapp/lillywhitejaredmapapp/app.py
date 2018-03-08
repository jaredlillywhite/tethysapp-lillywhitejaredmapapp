from tethys_sdk.base import TethysAppBase, url_map_maker


class Lillywhitejaredmapapp(TethysAppBase):
    """
    Tethys app class for Lillywhitejaredmapapp.
    """

    name = "Jared's Map App"
    index = 'lillywhitejaredmapapp:home'
    icon = 'lillywhitejaredmapapp/images/mapicon.jpg'
    package = 'lillywhitejaredmapapp'
    root_url = 'lillywhitejaredmapapp'
    color = '#27AE60'
    description = 'This is my map app with my name/'
    tags = 'Map'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='lillywhitejaredmapapp',
                controller='lillywhitejaredmapapp.controllers.home'
            ),
            UrlMap(
                name='mapview',
                url='mapview',
                controller='lillywhitejaredmapapp.controllers.mapview'
            ),
            UrlMap(
                name='dataservices',
                url='dataservices',
                controller='lillywhitejaredmapapp.controllers.dataservices'
            ),
            UrlMap(
                name='about',
                url='about',
                controller='lillywhitejaredmapapp.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='lillywhitejaredmapapp.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='mockup',
                controller='lillywhitejaredmapapp.controllers.mockup'
            )
        )

        return url_maps
