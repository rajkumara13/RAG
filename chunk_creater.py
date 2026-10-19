from typing import List
""" from pdf_reader import read_pdf """

def chunks_pages(pages:List[str],chunk_size:int =800,overlap:int=150)->List[str]:
    chunks=[]
    full_txt=" ".join(pages)
    txt_len=len(full_txt)

    if txt_len==0:
        return chunks
    start=0
    while(start<txt_len):
        end=min(start+chunk_size,txt_len)
        chunk=full_txt[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end>=txt_len:
            break
        start=end-overlap
        print(f"start:{start},end:{end},chunk_len:{len(chunk)}")
    return chunks
"""
obj=read_pdf("D:\clg project\RAG\pdf\Rajkumar1 Ai.pdf")
chunks=chunks_pages(obj)
print(chunks[3])

"""