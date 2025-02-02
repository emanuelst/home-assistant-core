"""The sensor tests for the nexia platform."""

from homeassistant.const import PERCENTAGE, UnitOfTemperature

from .util import async_init_integration


async def test_create_sensors(hass):
    """Test creation of sensors."""

    await async_init_integration(hass)

    state = hass.states.get("sensor.nick_office_temperature")
    assert state.state == "23"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "device_class": "temperature",
        "friendly_name": "Nick Office Temperature",
        "unit_of_measurement": UnitOfTemperature.CELSIUS,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.nick_office_zone_setpoint_status")
    assert state.state == "Permanent Hold"
    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Nick Office Zone Setpoint Status",
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.nick_office_zone_status")
    assert state.state == "Relieving Air"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Nick Office Zone Status",
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_air_cleaner_mode")
    assert state.state == "auto"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Master Suite Air Cleaner Mode",
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_current_compressor_speed")
    assert state.state == "69.0"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Master Suite Current Compressor Speed",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_outdoor_temperature")
    assert state.state == "30.6"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "device_class": "temperature",
        "friendly_name": "Master Suite Outdoor Temperature",
        "unit_of_measurement": UnitOfTemperature.CELSIUS,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_relative_humidity")
    assert state.state == "52.0"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "device_class": "humidity",
        "friendly_name": "Master Suite Relative Humidity",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_requested_compressor_speed")
    assert state.state == "69.0"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Master Suite Requested Compressor Speed",
        "unit_of_measurement": PERCENTAGE,
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )

    state = hass.states.get("sensor.master_suite_system_status")
    assert state.state == "Cooling"

    expected_attributes = {
        "attribution": "Data provided by Trane Technologies",
        "friendly_name": "Master Suite System Status",
    }
    # Only test for a subset of attributes in case
    # HA changes the implementation and a new one appears
    assert all(
        state.attributes[key] == expected_attributes[key] for key in expected_attributes
    )
