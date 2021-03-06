import pandas as pd

def metrics_to_csv(metrics, filepath):
    """ Writes metrics outputs to the file specified.

    Parameters
    ----------
    metrics : list of dict
        list of outputs from the function
        `thermostat.calculate_epa_draft_rccs_field_savings_metrics()`
    filepath : str
        filepath specification for location of output CSV file.

    Returns
    -------
    df : pd.DataFrame
        DataFrame containing data output to CSV.
    """

    columns = [
        'sw_version',

        'ct_identifier',
        'equipment_type',
        'heating_or_cooling',
        'zipcode',
        'station',
        'climate_zone',

        'start_date',
        'end_date',
        'n_days_in_inputfile_date_range',
        'n_days_both_heating_and_cooling',
        'n_days_insufficient_data',
        'n_core_cooling_days',
        'n_core_heating_days',

        'baseline_percentile_core_cooling_comfort_temperature',
        'baseline_percentile_core_heating_comfort_temperature',
        'regional_average_baseline_cooling_comfort_temperature',
        'regional_average_baseline_heating_comfort_temperature',

        'percent_savings_baseline_percentile',
        'avoided_daily_mean_core_day_runtime_baseline_percentile',
        'avoided_total_core_day_runtime_baseline_percentile',
        'baseline_daily_mean_core_day_runtime_baseline_percentile',
        'baseline_total_core_day_runtime_baseline_percentile',
        '_daily_mean_core_day_demand_baseline_baseline_percentile',
        'percent_savings_baseline_regional',
        'avoided_daily_mean_core_day_runtime_baseline_regional',
        'avoided_total_core_day_runtime_baseline_regional',
        'baseline_daily_mean_core_day_runtime_baseline_regional',
        'baseline_total_core_day_runtime_baseline_regional',
        '_daily_mean_core_day_demand_baseline_baseline_regional',
        'mean_demand',
        'alpha',
        'tau',
        'mean_sq_err',
        'root_mean_sq_err',
        'cv_root_mean_sq_err',
        'mean_abs_err',
        'mean_abs_pct_err',

        'total_core_cooling_runtime',
        'total_core_heating_runtime',
        'total_auxiliary_heating_core_day_runtime',
        'total_emergency_heating_core_day_runtime',

        'daily_mean_core_cooling_runtime',
        'daily_mean_core_heating_runtime',

        'core_cooling_days_mean_indoor_temperature',
        'core_cooling_days_mean_outdoor_temperature',
        'core_heating_days_mean_indoor_temperature',
        'core_heating_days_mean_outdoor_temperature',
        'core_mean_indoor_temperature',
        'core_mean_outdoor_temperature',

        'rhu_00F_to_05F',
        'rhu_05F_to_10F',
        'rhu_10F_to_15F',
        'rhu_15F_to_20F',
        'rhu_20F_to_25F',
        'rhu_25F_to_30F',
        'rhu_30F_to_35F',
        'rhu_35F_to_40F',
        'rhu_40F_to_45F',
        'rhu_45F_to_50F',
        'rhu_50F_to_55F',
        'rhu_55F_to_60F',
    ]

    output_dataframe = pd.DataFrame(metrics, columns=columns)
    output_dataframe.to_csv(filepath, index=False, columns=columns)
    return output_dataframe
