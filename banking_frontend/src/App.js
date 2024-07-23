import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Sidebar from './components/sidebar';
import ChatInterface from './components/ChatInterface';
import Dashboard from './components/Dashboard';
import UserManagement from './components/UserManagement';
import Transactions from './components/Transactions';
import EmployeeActivity from './components/EmployeeActivity';
import CustomerInformation from './components/CustomerInformation';
import CreditCardTransactions from './components/CreditCardTransactions';
import LoanInformation from './components/LoanInformation';
import AccountInformation from './components/AccountInformation';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <div className="main-content">
          <Switch>
            <Route path="/dashboard" component={Dashboard} />
            <Route path="/user-management" component={UserManagement} />
            <Route path="/transactions" component={Transactions} />
            <Route path="/employee-activity" component={EmployeeActivity} />
            <Route path="/customer-information" component={CustomerInformation} />
            <Route path="/credit-card-transactions" component={CreditCardTransactions} />
            <Route path="/loan-information" component={LoanInformation} />
            <Route path="/account-information" component={AccountInformation} />
            <Route path="/" exact component={ChatInterface} />
          </Switch>
        </div>
      </div>
    </Router>
  );
};

export default App;
