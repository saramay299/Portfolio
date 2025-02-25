'''
This script has been useful when myself or my coworkers had multiple layers that needed to be clipped based on different feature in another layer
These occasions were clips that we needed based on a subset from a larger set, such as a small group of counties in one state or some states but not all.
'''

aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps("Map")[0]
US_States = map.listLayers("US_States")[0]
footprint = map.listLayers("footprint_layer")[0]
footprint_counties = map.listLayers("footprint_counties")[0]
footprint_counties_whole_country = map.listLayers("footprint_counties_master")[0]
non_footprint_county_outline = map.listLayers("non_footprint_county_outline")[0]
Counties_Clip = map.listLayers("Counties_Clip")[0]

state_fips_list = []

for fips in state_fips_list:
    #query strings
    select_string = "STATE_FIPS = '{}'".format(fips)  
    footprint_counties_q = "STATEFP = '{}'".format(fips)
    
    #state and county selections
    cur_state = arcpy.SelectLayerByAttribute_management(US_States, 'NEW_SELECTION', select_string)
    footprint_counties_selection = arcpy.SelectLayerByAttribute_management(footprint_counties, 'NEW_SELECTION', footprint_counties_q)
    
    #selecting non footprint counties
    arcpy.SelectLayerByLocation_management(non_footprint_county_outline, 'HAVE_THEIR_CENTER_IN', cur_state, '0 Miles', 'NEW_SELECTION')
    non_footprint_counties_select = arcpy.SelectLayerByLocation_management(non_footprint_county_outline, 'HAVE_THEIR_CENTER_IN', footprint_counties_selection, '0 Miles','REMOVE_FROM_SELECTION')
    
    #selecting all counties in state
    Counties_Clip_select = arcpy.SelectLayerByLocation_management(Counties_Clip, 'HAVE_THEIR_CENTER_IN', cur_state, '0 Miles', 'NEW_SELECTION')
    
    
    #exporting
    out_no_footprint_counties = "no_footprint_counties_" + fips
    out_footprint_counties = "footprint_counties_" + fips
    full_county_clip = "Counties_clip_" + fips   

    clip_out_feature_class = "footprint_2025_counties_" + fips
    arcpy.analysis.Clip(in_features = footprint_counties_whole_country,
                        clip_features = cur_state,
                        out_feature_class = clip_out_feature_class,
                        cluster_tolerance = "")    
    
    
    clip_out_feature_class = "clipped_2025_footprint_" + fips
    arcpy.analysis.Clip(in_features = footprint,
                        clip_features = cur_state,
                        out_feature_class = clip_out_feature_class,
                        cluster_tolerance = "")
    
    arcpy.management.CopyFeatures(Counties_Clip_select, full_county_clip)
    arcpy.management.CopyFeatures(footprint_counties, out_footprint_counties)
    arcpy.management.CopyFeatures(non_footprint_county_outline, out_no_footprint_counties)
    