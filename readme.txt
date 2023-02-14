Αρχικά θα πρέπει να εγκαταστήσετε το Anaconda https://docs.anaconda.com/anaconda/install/

Στην συνέχεια το jupyter https://jupyter.org/install

Για το δικό μας environment:

Install environment:
conda env create -f numenv.yml

Activate environment:

Windows
conda activate numenv

Linux/Mac:
source activate numenv

Πλέον θα πρέπει να βλέπετε την ένδειξη (numenv) στο τερματικό. ( Οποιοδήποτε pip install εκτελέσετε από εδώ και πέρα αφορά το numenv. )

Εκτελέστε την εντολή:
jupyter notebook

Εάν δεν εμφανίζεται ο πυρήνας του περιβάλλοντος εκτελέστε

python -m ipykernel install --user --name=numenv

Τέλος θα  πρέπει να εγκαταστήσετε τη βιβλιοθήκη graphviz στο λειτουργικό σας. https://graphviz.org/download/