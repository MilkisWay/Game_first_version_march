surface_map=[]
"""surface_map=[
'                                                   ',   
'                                                   ',    
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'                                                   ',
'L                                                  ',  
'XX                                                 ',  
'XX                                                 ',    
'XX                        P                        ',    
'XX                                                 ',    
'XX                                                 ',    
'XX                                                 ', 
'XX                 V        V      V               ',    
'XX               XXXX     XXXX    XXXX             ',
'XX              XXXXXXXXXXXXXXXXXXXXXXX            ',
'XX             XXXXXXXXXXXXXXXXXXXXXXXXX           ']"""
with open("surfmapp.txt", "r") as f:
    for line in f:
        surface_map.append(line)

tile_size = 32
screen_width = 1920
screen_height = len(surface_map)*tile_size