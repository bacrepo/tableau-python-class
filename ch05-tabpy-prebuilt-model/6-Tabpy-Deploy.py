from tabpy.models.utils import setup_utils
import pandas as pd

def plus(_arg1, _arg2):

    c = list(zip(_arg1,_arg2))
    df = pd.DataFrame(c, columns=['col1','col2'])
    df['col3'] = df['col1'] + df['col2']
    return df['col3'].tolist()

if __name__ == "__main__":
    setup_utils.deploy_model("plus", plus, "Just make a plus")




