import pandas as pd
# 1. 读取 SNP 矩阵
snp_matrix = pd.read_csv('snp_matrix_all.csv', index_col=0)
# 2. 转为长格式（每行一对菌株）
snp_df = snp_matrix.stack().reset_index()
snp_df.columns = ['Strain1', 'Strain2', 'SNP_Distance']
# 3. 只保留 Strain1 < Strain2（避免重复，如 SRR1-SRR2 和 SRR2-SRR1）
snp_df = snp_df[snp_df['Strain1'] < snp_df['Strain2']].copy()
# 4. 筛选 SNP < 100
snp_df_filtered = snp_df[snp_df['SNP_Distance'] < 100]
# 5. 导出结果
snp_df_filtered.to_csv('snp_pairs_less_than_100.tsv', sep='\t', index=False)
print(f"✅ 找到 {len(snp_df_filtered)} 对 SNP < 100")
print(snp_df_filtered.head())
