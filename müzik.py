import spotify
from spotify.oauth2 import SpotifyOAuth

# Spotify Developer panelinden alacağın bilgileri buraya eklemelisin
CLIENT_ID = "SENIN_CLIENT_ID"
CLIENT_SECRET = "SENIN_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8888/callback"

# İzin kapsamı (Playlist okuma ve yazma izni)
SCOPE = "playlist-read-private playlist-modify-public playlist-modify-private"

def spotify_baglantisi_kur():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))
    return sp

def playlist_sarkilarini_cek(sp, playlist_url):
    # Playlist ID'sini URL'den ayıkla
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    
    results = sp.playlist_items(playlist_id)
    sarkilar = []
    
    for item in results['items']:
        track = item['track']
        sarkilar.append({
            "ad": track['name'],
            "sanatci": track['artists'][0]['name'],
            "uri": track['uri']
        })
    
    return sarkilar

def yeni_listeye_ekle(sp, hedef_playlist_id, sarkı_urileri):
    sp.playlist_add_items(hedef_playlist_id, sarkı_urileri)
    print("Şarkılar başarıyla yeni listeye eklendi!")

# Örnek Kullanım:
# sp = spotify_baglantisi_kur()
# sarkilar = playlist_sarkilarini_cek(sp, "BURAYA_KAYNAK_PLAYLIST_LINKI_GELIR")
# uri_listesi = [s["uri"] for s in sarkilar]
# yeni_listeye_ekle(sp, "HEDEF_PLAYLIST_ID", uri_listesi)
