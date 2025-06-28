from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/epf-calculator')
def epf_calculator():
    return render_template('epf_calculator.html')

@app.route('/about')
def about():
    return render_template('about.html')

def calculate_epf_balance(monthly_salary, current_age, retirement_age, 
                         epf_contribution_rate, annual_increase, interest_rate):
    """
    Calculate EPF maturity amount using the exact formula logic specified
    """
    years_to_retirement = retirement_age - current_age
    yearly_data = []
    
    # Initialize tracking variables
    current_monthly_salary = monthly_salary
    epf_balance = 0.0
    total_contribution = 0.0
    total_interest = 0.0
    
    # Main calculation loop
    for year in range(1, years_to_retirement + 1):
        # Calculate yearly EPF contribution
        yearly_contribution = current_monthly_salary * 12 * epf_contribution_rate
        
        # Calculate interest on existing balance (compound interest)
        interest_earned = epf_balance * interest_rate
        
        # Update EPF balance
        epf_balance = epf_balance + yearly_contribution + interest_earned
        
        # Update totals
        total_contribution += yearly_contribution
        total_interest += interest_earned
        
        # Store yearly data
        yearly_data.append({
            'year': current_age + year,
            'annual_contribution': round(yearly_contribution, 2),
            'interest_earned': round(interest_earned, 2),
            'epf_balance': round(epf_balance, 2)
        })
        
        # Increase salary for next year
        current_monthly_salary = current_monthly_salary * (1 + annual_increase)
    
    return {
        'total_contribution': round(total_contribution, 2),
        'interest_earned': round(total_interest, 2),
        'final_balance': round(epf_balance, 2),
        'yearly_data': yearly_data
    }

@app.route('/calculate-epf', methods=['POST'])
def calculate_epf():
    try:
        data = request.get_json()
        
        monthly_salary = float(data['monthly_salary'])
        current_age = int(data['current_age'])
        epf_contribution_rate = float(data['epf_contribution_rate']) / 100
        annual_increase = float(data['annual_increase']) / 100
        interest_rate = float(data['interest_rate']) / 100
        retirement_age = int(data['retirement_age'])
        
        # Use the improved calculation function
        result = calculate_epf_balance(
            monthly_salary=monthly_salary,
            current_age=current_age,
            retirement_age=retirement_age,
            epf_contribution_rate=epf_contribution_rate,
            annual_increase=annual_increase,
            interest_rate=interest_rate
        )
        
        return jsonify({
            'success': True,
            'final_amount': result['final_balance'],
            'total_contribution': result['total_contribution'],
            'total_interest': result['interest_earned'],
            'yearly_data': result['yearly_data']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# For Vercel deployment
app.debug = False

if __name__ == '__main__':
    app.run(debug=True) 