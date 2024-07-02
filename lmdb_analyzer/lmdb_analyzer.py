import lmdb
import argparse
import pickle
import json

def print_lmdb_content(env_path, encoding='utf-8', deserialization=None):
    # Ouvre l'environnement LMDB
    env = lmdb.open(env_path, readonly=True)

    with env.begin() as txn:
        # Ouvre un curseur pour parcourir la base de données
        cursor = txn.cursor()

        for key, value in cursor:
            key_decoded = key.decode(encoding)
            if deserialization == 'pickle':
                value_deserialized = pickle.loads(value)
            elif deserialization == 'json':
                value_deserialized = json.loads(value.decode(encoding))
            else:
                value_deserialized = value.decode(encoding)
            print(f'Clé: {key_decoded}, Valeur: {value_deserialized}')

    # Ferme l'environnement
    env.close()

def main():
    parser = argparse.ArgumentParser(description='Analyse une base de données LMDB et affiche son contenu.')
    parser.add_argument('path', type=str, help='Chemin vers la base de données LMDB')
    parser.add_argument('--encoding', type=str, default='utf-8', help='Encodage utilisé pour les clés et valeurs (par défaut: utf-8)')
    parser.add_argument('--deserialization', type=str, choices=['pickle', 'json'], help='Méthode de désérialisation des valeurs (pickle, json ou None)')

    args = parser.parse_args()
    print_lmdb_content(args.path, args.encoding, args.deserialization)

if __name__ == '__main__':
    main()
