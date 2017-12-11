# function used to generate scatterplot axis lists
def city_type_plots(type_df):
    city_type_sm = type_df.groupby('city').sum()
    city_type_ct = type_df.groupby('city').count()
    city_type_mn = type_df.groupby('city').mean()

    city_type_rides_axis = list(city_type_ct['driver_count'])
    city_type_fare_axis = list(city_type_mn['fare'])
    city_type_driver_axis = list((city_type_sm / city_type_ct)['driver_count'])

    return city_type_rides_axis, city_type_fare_axis, city_type_driver_axis

# function used to generate pie axis lists
def city_type_perc(type_df, city_type, city_ride_df):
    total_fare = city_ride_df['fare'].sum()
    city_type_fare = type_df.groupby('type').sum()['fare'][city_type]
    perc_total_fare = city_type_fare/total_fare

    total_count = len(city_ride_df)
    city_type_rides = type_df.groupby('type').count()['city'][city_type]
    perc_total_rides = city_type_rides/total_count

    total_drivers = city_ride_df.groupby([
        'type','driver_count']).count().reset_index().groupby('type').sum()['driver_count'].sum()
    city_type_drivers = type_df.groupby([
        'type','driver_count']).count().reset_index().groupby('type').sum()['driver_count'][city_type]
    perc_total_drivers = city_type_drivers/total_drivers

    return [perc_total_fare, perc_total_rides, perc_total_drivers]
