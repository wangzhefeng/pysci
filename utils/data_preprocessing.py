import numpy as np


def data_preprocessing(data, method, is_export_csv = 0):
    """
    data preprocessing
    """
    df = pd.DataFrame()
    if method == "origin":
        df = data.iloc[0:1440]
    elif method == "base":
        df = data.iloc[0:1440]
    elif method == "delta":
        df["eturb_m1_steam_flow_in"] = np.array(data["eturb_m1_steam_flow_in"].iloc[1:1441]) - np.array(data["eturb_m1_steam_flow_in"].iloc[0:1440])
        df["eturb_m1_steam_flow_side"] = np.array(data["eturb_m1_steam_flow_side"].iloc[1:1441]) - np.array(data["eturb_m1_steam_flow_side"].iloc[0:1440])
        df["eturb_m1_electricity_generation"] = np.array(data["eturb_m1_electricity_generation"].iloc[1:1441]) - np.array(data["eturb_m1_electricity_generation"].iloc[0:1440])
        df["eturb_m2_steam_flow_in"] = np.array(data["eturb_m2_steam_flow_in"].iloc[1:1441]) - np.array(data["eturb_m2_steam_flow_in"].iloc[0:1440])
        df["eturb_m2_steam_flow_side"] = np.array(data["eturb_m2_steam_flow_side"].iloc[1:1441]) - np.array(data["eturb_m2_steam_flow_side"].iloc[0:1440])
        df["eturb_m2_electricity_generation"] = np.array(data["eturb_m2_electricity_generation"].iloc[1:1441]) - np.array(data["eturb_m2_electricity_generation"].iloc[0:1440])
        df["bturb_m1_steam_flow_in"] = np.array(data["bturb_m1_steam_flow_in"].iloc[1:1441]) - np.array(data["bturb_m1_steam_flow_in"].iloc[0:1440])
        df["bturb_m1_electricity_generation"] = np.array(data["bturb_m1_electricity_generation"].iloc[1:1441]) - np.array(data["bturb_m1_electricity_generation"].iloc[0:1440])
        df = df.iloc[0:1440]
        if is_export_csv:
            df.to_csv(os.path.join(result_path, "raw_data.csv"), index = None)
    elif method == "mean":
        for i, j in zip(range(0, 1450, 10), range(60, 1450, 10)):
            temp_df = pd.DataFrame(data.iloc[i:j].mean(axis = 0))
            df = pd.concat([df, temp_df.transpose()], axis = 0, sort = False)
        df = df.iloc[0:1440]
    
    return df