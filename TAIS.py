{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3237f7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "carthage=\"https://pleiades.stoa.org/places/314921/json\" #pid de Carthage\n",
    "hippone=\"https://pleiades.stoa.org/places/305090/json\" #pid d'Hippone\n",
    "hippo_diarrhytus=\"https://pleiades.stoa.org/places/315038/json\" #pid d'Hippo Diarrhytus\n",
    "chusa=\"https://pleiades.stoa.org/places/619139/json\" #pid de Chusa\n",
    "milev=\"https://pleiades.stoa.org/places/305109/json\" #pid de Milev\n",
    "bulla_regia=\"https://pleiades.stoa.org/places/314912/json\" #pid de Bulla Regia\n",
    "utique=\"https://pleiades.stoa.org/places/315248/json\" #pid d'Utique\n",
    "thignica=\"https://pleiades.stoa.org/places/315207/json\" #pid de Thignica\n",
    "boseth=\"https://pleiades.stoa.org/places/321647/json\" #pid de Boseth\n",
    "thubuna=\"https://pleiades.stoa.org/places/334641/json\" #pid de Tuneba\n",
    "\n",
    "liste_lieux=[carthage, hippone, hippo_diarrhytus, chusa, milev, bulla_regia, utique, thignica, thubuna] \n",
    "#boseth non géolocalisée\n",
    "#chusa géolocalisée en Asie mineure...\n",
    "\n",
    "longitudes=[]\n",
    "latitudes=[]\n",
    "for i in liste_lieux:\n",
    "    response=requests.get(i).json()\n",
    "    coordinates=response['features'][0]['geometry']['coordinates']\n",
    "    longitudes.append(coordinates[0])\n",
    "    latitudes.append(coordinates[1])  \n",
    "    \n",
    "df=pd.read_csv(\"sermons_hors_Hippone.csv\")\n",
    "df[\"longitude\"]=\"\"\n",
    "df[\"latitude\"]=\"\"\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Carthage', 'longitude'] = longitudes[0]\n",
    "df.loc[df[\"lieu\"] == 'Carthage', 'latitude'] = latitudes[0]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Hippone', 'longitude'] = longitudes[1]\n",
    "df.loc[df[\"lieu\"] == 'Hippone', 'latitude'] = latitudes[1]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Hippo Diarrhytus', 'longitude'] = longitudes[2]\n",
    "df.loc[df[\"lieu\"] == 'Hippo Diarrhytus', 'latitude'] = latitudes[2]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Milev', 'longitude'] = longitudes[4]\n",
    "df.loc[df[\"lieu\"] == 'Milev', 'latitude'] = latitudes[4]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Bulla Regia', 'longitude'] = longitudes[5]\n",
    "df.loc[df[\"lieu\"] == 'Bulla Regia', 'latitude'] = latitudes[5]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Utique', 'longitude'] = longitudes[6]\n",
    "df.loc[df[\"lieu\"] == 'Utique', 'latitude'] = latitudes[6]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Thignica', 'longitude'] = longitudes[7]\n",
    "df.loc[df[\"lieu\"] == 'Thignica', 'latitude'] = latitudes[7]\n",
    "\n",
    "df.loc[df[\"lieu\"] == 'Thubuna', 'longitude'] = longitudes[8]\n",
    "df.loc[df[\"lieu\"] == 'Thubuna', 'latitude'] = latitudes[8]\n",
    "\n",
    "df.to_csv(\"sermons_hors_Hippo.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "e968aa32",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"lieu\"].value_counts()\n",
    "df[\"count\"]=df['lieu'].map(df[\"lieu\"].value_counts())\n",
    "df = df.dropna(subset=['count'])\n",
    "df['count'] = df['count'].apply(int)\n",
    "df.to_csv(\"count_hors_Hippo.csv\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
