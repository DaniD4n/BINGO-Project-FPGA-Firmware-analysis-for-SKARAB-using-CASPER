import numpy as np
import h5py
from astropy.io import fits
import os



# 1. Ler vários arquivos .npz de um diretório, concatenar e ordenar---------------------------------
def concat_npz(diretorio_npz, saida_npz):
    """
    Lê todos os .npz do diretório, concatena os dados,
    faz sorted pelo tempo e salva em um NPZ final.
    """
    dafft_total = []
    tempo_total = []

    arquivos = sorted(
        [f for f in os.listdir(diretorio_npz) if f.endswith(".npz")]
    )

    if not arquivos:
        raise ValueError("Nenhum arquivo .npz encontrado no diretório.")

    print(f"Encontrados {len(arquivos)} arquivos .npz")

    for arq in arquivos:
        path = os.path.join(diretorio_npz, arq)
        dados = np.load(path)

        dafft_total.append(dados["dafft"])
        tempo_total.append(dados["tempo"])

    # Concatena tudo
    dafft_total = np.concatenate(dafft_total)
    tempo_total = np.concatenate(tempo_total)

    # Ordenação por tempo
    ordem = np.argsort(tempo_total)
    tempo_total = tempo_total[ordem]
    dafft_total = dafft_total[ordem]

    # Salvar
    np.savez(saida_npz, dafft=dafft_total, tempo=tempo_total)

    print(f"NPZ final gerado e ordenado: {saida_npz}")



# 2. Exportar NPZ -> HDF5------------------------------------------------------
def npz_to_hdf5(npz_path, hdf5_path):
    dados = np.load(npz_path)
    dafft = dados["dafft"]
    tempo = dados["tempo"]

    with h5py.File(hdf5_path, "w") as h5:
        h5.create_dataset("dafft", data=dafft)
        h5.create_dataset("tempo", data=tempo)

    print(f"Arquivo HDF5 gerado: {hdf5_path}")



# 3. Exportar NPZ -> FITS-----------------------------------------------------------
def npz_to_fits(npz_path, fits_path):
    dados = np.load(npz_path)
    dafft = dados["dafft"]
    tempo = dados["tempo"]

    col1 = fits.Column(name="dafft", format="D", array=dafft)
    col2 = fits.Column(name="tempo", format="D", array=tempo)

    hdu = fits.BinTableHDU.from_columns([col1, col2])
    hdu.writeto(fits_path, overwrite=True)

    print(f"Arquivo FITS gerado: {fits_path}")
