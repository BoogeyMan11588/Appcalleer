import streamlit as st
import socket
import requests

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except OSError:
        return False

def update_status(host, port):
    return "Heartbeat" if check_port(host, port) else "No Heartbeat"

def update_players_info(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        players = response.json()
        return "\n".join([f"Player: {player['name']}, Ping: {player['ping']}" for player in players]) if players else "No Players"
    except requests.RequestException:
        return "N/A City Down"

def update_server_info():
    url = "http://108.15.30.30:30120/info.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        info = response.json()
        txadmin_version = info['vars'].get('txAdmin-version', 'Unknown')
        return txadmin_version
    except (requests.RequestException, KeyError):
        return "N/A City Down", "N/A"

def check_version(current_version):
    url = "https://api.github.com/repos/tabarra/txAdmin/releases/latest"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        latest_release = response.json()
        latest_version = latest_release['tag_name'].lstrip('v')  
        return "red" if version_tuple(current_version) < version_tuple(latest_version) else "black"
    except requests.RequestException:
        return "orange"

def version_tuple(version):
    return tuple(map(int, version.split('.')))

# Streamlit layout
st.title("Mission Control for FiveM Servers")

st.header("RTC")
rtc_status = update_status("108.15.30.30", 30120)
st.markdown(f"**RTC Status**: <span style='color:{'green' if rtc_status == 'Heartbeat' else 'red'}'>{rtc_status}</span>", unsafe_allow_html=True)

st.header("Unrivaled")
unrivaled_status = update_status("108.15.30.30", 30121)
st.markdown(f"**Unrivaled Status**: <span style='color:{'green' if unrivaled_status == 'Heartbeat' else 'red'}'>{unrivaled_status}</span>", unsafe_allow_html=True)

st.header("Server Info")
txadmin_version = update_server_info()
st.markdown(f"**txAdmin Version**: <span style='color:{check_version(txadmin_version)}'>{txadmin_version}</span>", unsafe_allow_html=True)

st.header("Attendance - RTC")
rtc_players_info = update_players_info("http://108.15.30.30:30120/players.json")
st.text(rtc_players_info)

st.header("Attendance - Unrivaled")
unrivaled_players_info = update_players_info("http://108.15.30.30:30121/players.json")
st.text(unrivaled_players_info)
