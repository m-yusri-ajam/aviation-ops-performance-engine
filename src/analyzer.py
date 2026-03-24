import pandas as pd

def run_ops_analysis():
    # 1. Load the generated flight logs
    df = pd.read_csv('data/a350_ops_logs.csv')

    # 2. Calculate On-Time Performance (OTP)
    # Aviation Standard: OTP is a departure within 15 mins of schedule
    df['is_on_time'] = (df['Delay_Min'] <= 15).astype(int)
    overall_otp = df['is_on_time'].mean() * 100

    # 3. Calculating Turnaround Leakage Cost
    # Assumption that every minute costs roughly 150 AED in airport fees/crew
    df['Delay_Cost_AED'] = df['Delay_Min'] * 150
    total_leakage = df['Delay_Cost_AED'].sum()

    # 4. Vendor Ranking (Performance Scorecard)
    vendor_perf = df.groupby('Vendor').agg({
        'is_on_time': 'mean',
        'Delay_Min': 'mean',
        'Fuel_Variance_AED': 'sum'
    }).rename(columns={'is_on_time': 'OTP_Rate'}).sort_values(by='OTP_Rate', ascending=False)

    # 5. Export for Looker Studio
    import os
    if not os.path.exists('reports'):
        os.makedirs('reports')
        
    df.to_csv('reports/master_ops-report.csv', index=False)

    print("-" * 30)
    print(f"OPS ANALYSIS COMPLETE")
    print(f"Overall Network OTP: {overall_otp:.1f}")
    print(f"Total Turnaround Leakage: {total_leakage:.2f} AED")
    print("-" * 30)
    print(vendor_perf)

if __name__ == "__main__":
    run_ops_analysis()