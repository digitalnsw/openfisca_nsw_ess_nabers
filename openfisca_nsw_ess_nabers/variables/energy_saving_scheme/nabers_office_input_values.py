# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
import numpy as np

# measured_electricity_consumption input at Step 1
# measured_gas_consumption input at Step 1
# onsite_unaccounted_electricity input at Step 1
# nabers_electricity input at Step 1
# hours_per_week_with_20_percent_occupancy input at Step 3
# net_lettable_area input at Step 3
# building_area_type input at Step 3

# coal_in_KG input in unit_conversions
# coal_KG_to_kWh input in unit_conversions
# diesel_in_L input in unit_conversions
# diesel_in_kWh KG input in unit_conversions
# gas_in_MJ input in unit_conversions
# gas_MJ_to_kWh input in unit_conversions

# add from filename import function to init.py

# note that this file is used to store user inputs. Everything in this file
# should be input by the user and is publicly accessible.


class offices_postcode:
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'The postcode for the relevant NABERS building.'

    def formula(buildings, period, parameters):
        return (buildings('postcode', period))


class number_of_computers(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The number of computers registered as used within the NABERS rating"


class rating_type(Variable):
    value_type = str
    entity = Building
    definition_period = ETERNITY
    label = 'The type of building rated within the NABERS Office suite. Also' \
            ' used to determine which reverse calculator is used.'


class benchmark_star_rating(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY  # need to check whether these inputs, on the NABERS reports, should all be year
    label = 'The star rating for which the benchmark electricity and gas' \
            'consumption is calculated against - what NABERS rating the' \
            ' building aims to achieve.'

    def formula(buildings, period, parameters):
        return buildings('method_one', period)


class building_state_location(Variable):
    value_type = str
    entity = Building
    definition_period = ETERNITY
    label = "State within which the relevant NABERS rated building is located."


class elec_kWh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The electricity consumption of the building, in kWh, as detailed on the NABERS report"


class gas_kWh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The gas consumption of the building, in kWh, as detailed on the NABERS report"

    def formula(buildings, period, parameters):
        return buildings('gas_MJ_to_KWh', period)


class diesel_kWh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The oil consumption of the building, in kWh, as detailed on the NABERS report"

    def formula(buildings, period, parameters):
        return buildings('diesel_litres_to_KWh', period)


class coal_kWh (Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The coal consumption of the building, in kWh, as detailed on the NABERS report"

    def formula(buildings, period, parameters):
        return buildings('coal_KG_to_KWh', period)


class total_energy_kwh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The total kWh consumption of the building, summing electricity, gas, oil and diesel, expressed in kWh"

    def formula(buildings, period, parameters):
        return buildings('elec_kWh', period) + buildings('gas_kWh', period) + buildings('coal_kWh', period) + buildings('diesel_kWh', period)


class perc_elec_kwh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The percentage of a building's energy consumption that is derived from its electricity consumption, expressed as a percentage of total energy use to 2 decimal places"

    def formula(buildings, period, parameters):
        elec_percent = buildings('elec_kWh', period) / buildings('total_energy_kwh', period) * 100
        return np.round(elec_percent, 3)


class perc_gas_kwh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The percentage of a building's energy consumption that is derived from its electricity consumption, expressed as a percentage of total energy use to 2 decimal places"

    def formula(buildings, period, parameters):
        gas_percent = buildings('gas_kWh', period) / buildings('total_energy_kwh', period) * 100
        return np.round(gas_percent, 3)


class perc_diesel_kwh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The percentage of a building's energy consumption that is derived from its diesel consumption, expressed as a percentage of total energy use to 2 decimal places"

    def formula(buildings, period, parameters):
        diesel_percent = buildings('diesel_kWh', period) / buildings('total_energy_kwh', period) * 100
        return np.round(diesel_percent, 3)


class perc_coal_kwh(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = "The percentage of a building's energy consumption that is derived from its oil consumption, expressed as a percentage of total energy use to 2 decimal places"

    def formula(buildings, period, parameters):
        coal_percent = buildings('coal_kWh', period) / buildings('total_energy_kwh', period) * 100
        return np.round(coal_percent, 3)
