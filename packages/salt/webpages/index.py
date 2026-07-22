# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'plainindex'
    
    @property
    def index_url(self):
        return None

    def index_dashboard(self, root):


        wrapper = root.div(width='100%', height='100%',
                           text_align='center', background='white',
                           padding_top='30px')
        wrapper.img(src='/_pkg/salt/resources/html_pages/images/Ranalli_Logo.svg',
                    style='width:20%;margin-top:30px;')

        titlebox = wrapper.div(display='flex',
                               justify_content='center',
                               align_items='center',
                               gap='20px',
                               margin_top='20px',
                               margin_bottom='30px')

        titlebox.img(src='/_pkg/salt/resources/html_pages/images/salt.svg',
                     style='width:100px;height:100px;')

        titlebox.div(
                'Movimentazione Sale<br>ITALKALI</br>',
                font_size='60px',
                font_weight='bold',
                color='#384D63',
                text_shadow='2px 2px 4px rgba(0,0,0,0.15)')


        #titlebox.div('Shipsteps', font_size='100px', color='#384D63')


