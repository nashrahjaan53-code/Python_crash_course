import os

# Create directories
os.makedirs("src/components", exist_ok=True)
os.makedirs("src/pages", exist_ok=True)

# 1. Update package.json
package_json = '''{
  "name": "digital-ration-system",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.6.2",
    "chart.js": "^4.4.0",
    "framer-motion": "^10.16.4",
    "react": "^18.2.0",
    "react-chartjs-2": "^5.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^4.12.0",
    "react-router-dom": "^6.20.0",
    "react-scripts": "5.0.1",
    "tailwindcss": "^3.3.5",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31"
  }
}'''

# 2. Tailwind config
tailwind_config = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'gov-blue': '#1e3a8a',
        'gov-green': '#065f46',
        'ration-orange': '#ea580c',
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'scan': 'scan 2s linear infinite',
      },
      keyframes: {
        scan: {
          '0%': { transform: 'translateY(-100%)' },
          '100%': { transform: 'translateY(100%)' },
        }
      }
    },
  },
  plugins: [],
}'''

# 3. PostCSS config
postcss_config = '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}'''

# 4. index.css
index_css = '''@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-gray-50 text-gray-900;
  }
}

@layer components {
  .card {
    @apply bg-white rounded-xl shadow-lg p-6 border border-gray-200;
  }
  
  .btn-primary {
    @apply bg-gov-blue text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-800 transition duration-300;
  }
  
  .btn-secondary {
    @apply bg-gov-green text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-800 transition duration-300;
  }
  
  .input-field {
    @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-gov-blue focus:border-transparent outline-none;
  }
}'''

# 5. App.js
app_js = '''import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Verify from './pages/Verify';
import Shop from './pages/Shop';
import Orders from './pages/Orders';
import Admin from './pages/Admin';
import Login from './pages/Login';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [userType, setUserType] = useState('user');

  const handleLogin = (type) => {
    setIsAuthenticated(true);
    setUserType(type);
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setUserType('user');
  };

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        {isAuthenticated ? (
          <>
            <Navbar isAdmin={userType === 'admin'} />
            <Routes>
              {userType === 'user' ? (
                <>
                  <Route path="/dashboard" element={<Dashboard />} />
                  <Route path="/verify" element={<Verify />} />
                  <Route path="/shop" element={<Shop />} />
                  <Route path="/orders" element={<Orders />} />
                  <Route path="/" element={<Navigate to="/dashboard" />} />
                </>
              ) : (
                <>
                  <Route path="/admin" element={<Admin />} />
                  <Route path="/" element={<Navigate to="/admin" />} />
                </>
              )}
              <Route path="*" element={<Navigate to={userType === 'user' ? "/dashboard" : "/admin"} />} />
            </Routes>
            
            <footer className="mt-12 bg-gray-900 text-white py-8">
              <div className="container mx-auto px-4">
                <div className="flex flex-col md:flex-row justify-between items-center">
                  <div>
                    <h2 className="text-2xl font-bold mb-2">Digital Ration System</h2>
                    <p className="text-gray-400">A prototype for modern PDS distribution</p>
                  </div>
                  <div className="mt-4 md:mt-0">
                    <p className="text-gray-400 text-sm">
                      This is a demo system. Real implementation requires UIDAI integration.
                    </p>
                    <div className="flex space-x-4 mt-2">
                      <span className="px-3 py-1 bg-blue-900 text-blue-200 rounded text-sm">React</span>
                      <span className="px-3 py-1 bg-green-900 text-green-200 rounded text-sm">Node.js</span>
                      <span className="px-3 py-1 bg-purple-900 text-purple-200 rounded text-sm">Aadhaar API</span>
                    </div>
                  </div>
                </div>
                <div className="border-t border-gray-800 mt-6 pt-6 text-center text-gray-500 text-sm">
                  <p>© 2024 Digital Ration System Prototype. For demonstration purposes only.</p>
                  <p className="mt-1">Part of Digital India Initiative • SIH 2024 Submission</p>
                </div>
              </div>
            </footer>
          </>
        ) : (
          <Login onLogin={handleLogin} />
        )}
      </div>
    </Router>
  );
}

export default App;'''

# 6. index.js
index_js = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);'''

# 7. Navbar.jsx (simplified version)
navbar_jsx = '''import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaHome, FaFingerprint, FaShoppingCart, FaHistory, FaSignOutAlt } from 'react-icons/fa';

const Navbar = ({ isAdmin = false }) => {
  const location = useLocation();
  
  const userNavItems = [
    { path: '/dashboard', label: 'Dashboard', icon: <FaHome /> },
    { path: '/verify', label: 'Verify', icon: <FaFingerprint /> },
    { path: '/shop', label: 'Ration Shop', icon: <FaShoppingCart /> },
    { path: '/orders', label: 'My Orders', icon: <FaHistory /> },
  ];
  
  const adminNavItems = [
    { path: '/admin', label: 'Dashboard', icon: <FaHome /> },
    { path: '/admin/orders', label: 'Orders', icon: <FaShoppingCart /> },
    { path: '/admin/inventory', label: 'Inventory', icon: <FaHistory /> },
  ];
  
  const navItems = isAdmin ? adminNavItems : userNavItems;
  
  return (
    <nav className="bg-gov-blue text-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center py-4">
          <div className="flex items-center space-x-2">
            <div className="bg-white p-2 rounded-lg">
              <FaFingerprint className="text-gov-blue text-2xl" />
            </div>
            <h1 className="text-2xl font-bold">
              Digital Ration System
              {isAdmin && <span className="text-sm ml-2 bg-ration-orange px-2 py-1 rounded">Admin</span>}
            </h1>
          </div>
          
          <div className="flex items-center space-x-6">
            {navItems.map((item) => (
              <Link
                key={item.path}
                to={item.path}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition ${
                  location.pathname === item.path ? 'bg-blue-800' : 'hover:bg-blue-700'
                }`}
              >
                {item.icon}
                <span>{item.label}</span>
              </Link>
            ))}
            
            <button className="flex items-center space-x-2 px-4 py-2 bg-red-600 rounded-lg hover:bg-red-700 transition">
              <FaSignOutAlt />
              <span>Logout</span>
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;'''

# 8. Login.jsx (simplified)
login_jsx = '''import React, { useState } from 'react';
import { FaUser, FaStore } from 'react-icons/fa';

const Login = ({ onLogin }) => {
  const [loginType, setLoginType] = useState('user');

  return (
    <div className="min-h-screen bg-gradient-to-br from-gov-blue to-gov-green flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-800">Digital Ration System</h2>
          <p className="text-gray-600 mt-2">Login to continue</p>
        </div>

        <div className="flex space-x-4 mb-8">
          <button
            onClick={() => setLoginType('user')}
            className={`flex-1 py-4 rounded-xl border-2 flex flex-col items-center justify-center transition ${
              loginType === 'user'
                ? 'border-gov-blue bg-blue-50'
                : 'border-gray-200 hover:border-gray-300'
            }`}
          >
            <FaUser className={`text-2xl mb-2 ${loginType === 'user' ? 'text-gov-blue' : 'text-gray-400'}`} />
            <span className={`font-semibold ${loginType === 'user' ? 'text-gov-blue' : 'text-gray-600'}`}>
              Citizen
            </span>
          </button>
          
          <button
            onClick={() => setLoginType('admin')}
            className={`flex-1 py-4 rounded-xl border-2 flex flex-col items-center justify-center transition ${
              loginType === 'admin'
                ? 'border-gov-green bg-green-50'
                : 'border-gray-200 hover:border-gray-300'
            }`}
          >
            <FaStore className={`text-2xl mb-2 ${loginType === 'admin' ? 'text-gov-green' : 'text-gray-400'}`} />
            <span className={`font-semibold ${loginType === 'admin' ? 'text-gov-green' : 'text-gray-600'}`}>
              Shopkeeper
            </span>
          </button>
        </div>

        {loginType === 'user' ? (
          <div className="space-y-4">
            <div>
              <label className="block text-gray-700 mb-2">Ration Card Number</label>
              <input
                type="text"
                placeholder="Enter ration card number"
                className="input-field"
              />
            </div>
            <div>
              <label className="block text-gray-700 mb-2">Aadhaar Number</label>
              <input
                type="text"
                placeholder="Enter Aadhaar number"
                className="input-field"
              />
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            <div>
              <label className="block text-gray-700 mb-2">Shop ID</label>
              <input
                type="text"
                placeholder="Enter shop ID"
                className="input-field"
              />
            </div>
            <div>
              <label className="block text-gray-700 mb-2">Password</label>
              <input
                type="password"
                placeholder="Enter password"
                className="input-field"
              />
            </div>
          </div>
        )}

        <button
          onClick={() => onLogin(loginType)}
          className="w-full btn-primary py-4 text-lg mt-6"
        >
          Login to System
        </button>

        <div className="mt-8 pt-8 border-t">
          <p className="text-center text-gray-600 mb-4">Quick Demo Access</p>
          <div className="grid grid-cols-2 gap-4">
            <button
              onClick={() => onLogin('user')}
              className="py-3 bg-gradient-to-r from-gov-blue to-blue-600 text-white rounded-lg hover:from-blue-700 hover:to-blue-800 transition"
            >
              Demo as Citizen
            </button>
            <button
              onClick={() => onLogin('admin')}
              className="py-3 bg-gradient-to-r from-gov-green to-green-600 text-white rounded-lg hover:from-green-700 hover:to-green-800 transition"
            >
              Demo as Shopkeeper
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;'''

# 9. Dashboard.jsx (basic)
dashboard_jsx = '''import React from 'react';
import { FaUserCircle, FaCheckCircle, FaBoxOpen } from 'react-icons/fa';

const Dashboard = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">Citizen Dashboard</h1>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="card">
          <div className="flex items-center space-x-4 mb-6">
            <FaUserCircle className="text-6xl text-gov-blue" />
            <div>
              <h2 className="text-2xl font-bold">Rajesh Kumar</h2>
              <p className="text-gray-600">Ration Card Holder</p>
              <span className="inline-flex items-center mt-1 text-sm text-green-600">
                <FaCheckCircle className="mr-1" />
                Verified Citizen
              </span>
            </div>
          </div>
          
          <div className="space-y-4">
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Ration Card No</span>
              <span className="font-mono font-bold">DL/2023/567890</span>
            </div>
            <div className="flex justify-between py-2 border-b">
              <span className="text-gray-600">Family Size</span>
              <span className="font-bold">5 members</span>
            </div>
            <div className="flex justify-between py-2">
              <span className="text-gray-600">Monthly Quota</span>
              <span className="font-bold">55% remaining</span>
            </div>
          </div>
        </div>
        
        <div className="lg:col-span-2">
          <div className="card">
            <h3 className="text-xl font-bold mb-6">Recent Orders</h3>
            <div className="space-y-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="flex items-center justify-between p-4 border rounded-lg hover:bg-gray-50">
                  <div>
                    <p className="font-semibold">Order #{i}</p>
                    <p className="text-sm text-gray-600">Rice 5kg, Wheat 4kg</p>
                  </div>
                  <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm">
                    Delivered
                  </span>
                </div>
              ))}
            </div>
          </div>
          
          <div className="mt-6 card">
            <h3 className="text-xl font-bold mb-4">Monthly Quota Status</h3>
            <div className="space-y-4">
              <div>
                <div className="flex justify-between text-sm mb-1">
                  <span>Rice (5kg)</span>
                  <span>3kg used</span>
                </div>
                <div className="h-3 bg-gray-200 rounded-full overflow-hidden">
                  <div className="h-full bg-green-500" style={{ width: '60%' }}></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between text-sm mb-1">
                  <span>Wheat (4kg)</span>
                  <span>2kg used</span>
                </div>
                <div className="h-3 bg-gray-200 rounded-full overflow-hidden">
                  <div className="h-full bg-blue-500" style={{ width: '50%' }}></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;'''

# 10. Admin.jsx (basic)
admin_jsx = '''import React from 'react';
import { FaStore, FaBoxes, FaUsers } from 'react-icons/fa';

const Admin = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800">Shopkeeper Dashboard</h1>
        <p className="text-gray-600">Manage ration distribution for Shop #DL-42</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="card">
          <div className="flex items-center">
            <div className="p-3 bg-blue-100 rounded-lg mr-4">
              <FaStore className="text-2xl text-gov-blue" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Today's Orders</p>
              <p className="text-2xl font-bold">12</p>
            </div>
          </div>
        </div>
        
        <div className="card">
          <div className="flex items-center">
            <div className="p-3 bg-green-100 rounded-lg mr-4">
              <FaBoxes className="text-2xl text-gov-green" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Pending Delivery</p>
              <p className="text-2xl font-bold">4</p>
            </div>
          </div>
        </div>
        
        <div className="card">
          <div className="flex items-center">
            <div className="p-3 bg-yellow-100 rounded-lg mr-4">
              <FaUsers className="text-2xl text-yellow-600" />
            </div>
            <div>
              <p className="text-sm text-gray-600">Customers Today</p>
              <p className="text-2xl font-bold">24</p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="card">
        <h2 className="text-2xl font-bold mb-6">Today's Orders</h2>
        <div className="space-y-4">
          {[1, 2, 3].map((i) => (
            <div key={i} className="border rounded-lg p-4 hover:bg-gray-50">
              <div className="flex justify-between items-start mb-3">
                <div>
                  <h3 className="font-bold text-lg">Order #{i}</h3>
                  <p className="text-gray-600">Customer Name</p>
                </div>
                <span className="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full text-sm">
                  Processing
                </span>
              </div>
              <div className="mb-4">
                <p className="text-gray-700">Rice 5kg, Wheat 4kg, Sugar 2kg</p>
                <p className="text-sm text-gray-500 mt-1">Time: 10:30 AM • Amount: ₹0</p>
              </div>
              <div className="flex space-x-3">
                <button className="px-4 py-2 bg-gov-blue text-white rounded-lg hover:bg-blue-700">
                  Process Order
                </button>
                <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Admin;'''

# 11. Other pages (simplified)
verify_jsx = '''import React from 'react';

const Verify = () => {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          Biometric Verification
        </h1>
        <p className="text-gray-600 text-lg">
          This page will have fingerprint scanner simulation
        </p>
      </div>
    </div>
  );
};

export default Verify;'''

shop_jsx = '''import React from 'react';

const Shop = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">Digital Ration Shop</h1>
        <p className="text-gray-600">This page will have ration items for purchase</p>
      </div>
    </div>
  );
};

export default Shop;'''

orders_jsx = '''import React from 'react';

const Orders = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">My Orders</h1>
        <p className="text-gray-600">This page will show order history</p>
      </div>
    </div>
  );
};

export default Orders;'''

# Write all files
files = {
    "package.json": package_json,
    "tailwind.config.js": tailwind_config,
    "postcss.config.js": postcss_config,
    "src/index.css": index_css,
    "src/App.js": app_js,
    "src/index.js": index_js,
    "src/components/Navbar.jsx": navbar_jsx,
    "src/pages/Login.jsx": login_jsx,
    "src/pages/Dashboard.jsx": dashboard_jsx,
    "src/pages/Admin.jsx": admin_jsx,
    "src/pages/Verify.jsx": verify_jsx,
    "src/pages/Shop.jsx": shop_jsx,
    "src/pages/Orders.jsx": orders_jsx,
}

print("Creating files for Digital Ration System...")
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Created: {filepath}")

print("\\n✅ All files created successfully!")
print("\\n🚀 To start the application, run:")
print("npm start")




python -c 
import os

print('🚀 FIXING DIGITAL RATION SYSTEM...')

# Create fresh index.js
with open('src/index.js', 'w', encoding='utf-8') as f:
    f.write('''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
''')
print('✅ Created: src/index.js')

# Create fresh App.js
with open('src/App.js', 'w', encoding='utf-8') as f:
    f.write('''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function Home() {
  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-8'>
      <div className='max-w-6xl mx-auto'>
        <h1 className='text-4xl md:text-5xl font-bold text-blue-800 mb-6'>
          🚀 Digital Ration System
        </h1>
        <p className='text-xl text-gray-700 mb-10'>
          A modern solution for Public Distribution System with biometric authentication
        </p>
        
        <div className='grid grid-cols-1 md:grid-cols-3 gap-6 mb-12'>
          <div className='bg-white p-6 rounded-xl shadow-lg border border-blue-200'>
            <h3 className='text-2xl font-bold text-blue-600 mb-4'>For Citizens</h3>
            <ul className='space-y-3'>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Biometric Authentication
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Digital Ration Ordering
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                No More Queues
              </li>
            </ul>
            <button className='mt-6 w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700'>
              Login as Citizen
            </button>
          </div>
          
          <div className='bg-white p-6 rounded-xl shadow-lg border border-green-200'>
            <h3 className='text-2xl font-bold text-green-600 mb-4'>For Shopkeepers</h3>
            <ul className='space-y-3'>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Digital Inventory
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Order Management
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Automated Reporting
              </li>
            </ul>
            <button className='mt-6 w-full bg-green-600 text-white py-3 rounded-lg hover:bg-green-700'>
              Login as Shopkeeper
            </button>
          </div>
          
          <div className='bg-white p-6 rounded-xl shadow-lg border border-orange-200'>
            <h3 className='text-2xl font-bold text-orange-600 mb-4'>Benefits</h3>
            <ul className='space-y-3'>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                90% Less Corruption
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Real-time Tracking
              </li>
              <li className='flex items-center'>
                <span className='text-green-500 mr-2'>✓</span>
                Transparent System
              </li>
            </ul>
            <button className='mt-6 w-full bg-orange-600 text-white py-3 rounded-lg hover:bg-orange-700'>
              View Demo
            </button>
          </div>
        </div>
        
        <div className='bg-blue-100 border border-blue-300 rounded-xl p-6'>
          <h3 className='text-2xl font-bold text-blue-800 mb-4'>How It Works</h3>
          <div className='grid grid-cols-1 md:grid-cols-4 gap-4'>
            <div className='text-center'>
              <div className='w-16 h-16 bg-blue-500 text-white rounded-full flex items-center justify-center mx-auto mb-3 text-2xl'>1</div>
              <p className='font-semibold'>Biometric Scan</p>
            </div>
            <div className='text-center'>
              <div className='w-16 h-16 bg-green-500 text-white rounded-full flex items-center justify-center mx-auto mb-3 text-2xl'>2</div>
              <p className='font-semibold'>Select Items</p>
            </div>
            <div className='text-center'>
              <div className='w-16 h-16 bg-orange-500 text-white rounded-full flex items-center justify-center mx-auto mb-3 text-2xl'>3</div>
              <p className='font-semibold'>Shop Processes</p>
            </div>
            <div className='text-center'>
              <div className='w-16 h-16 bg-purple-500 text-white rounded-full flex items-center justify-center mx-auto mb-3 text-2xl'>4</div>
              <p className='font-semibold'>Home Delivery</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
''')
print('✅ Created: src/App.js')

# Create Login page
os.makedirs('src/pages', exist_ok=True)
with open('src/pages/Login.jsx', 'w', encoding='utf-8') as f:
    f.write('''import React, { useState } from 'react';

const Login = ({ onLogin }) => {
  const [loginType, setLoginType] = useState('user');

  return (
    <div className='min-h-screen bg-gradient-to-br from-blue-600 to-green-600 flex items-center justify-center p-4'>
      <div className='bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full'>
        <div className='text-center mb-8'>
          <h2 className='text-3xl font-bold text-gray-800'>Digital Ration System</h2>
          <p className='text-gray-600 mt-2'>Login to continue</p>
        </div>

        <div className='flex space-x-4 mb-8'>
          <button
            onClick={() => setLoginType('user')}
            className={\`flex-1 py-4 rounded-xl border-2 flex flex-col items-center justify-center transition \${
              loginType === 'user'
                ? 'border-blue-600 bg-blue-50'
                : 'border-gray-200 hover:border-gray-300'
            }\`}
          >
            <span className={\`text-2xl mb-2 \${loginType === 'user' ? 'text-blue-600' : 'text-gray-400'}\`}>👤</span>
            <span className={\`font-semibold \${loginType === 'user' ? 'text-blue-600' : 'text-gray-600'}\`}>
              Citizen
            </span>
          </button>
          
          <button
            onClick={() => setLoginType('admin')}
            className={\`flex-1 py-4 rounded-xl border-2 flex flex-col items-center justify-center transition \${
              loginType === 'admin'
                ? 'border-green-600 bg-green-50'
                : 'border-gray-200 hover:border-gray-300'
            }\`}
          >
            <span className={\`text-2xl mb-2 \${loginType === 'admin' ? 'text-green-600' : 'text-gray-400'}\`}>🏪</span>
            <span className={\`font-semibold \${loginType === 'admin' ? 'text-green-600' : 'text-gray-600'}\`}>
              Shopkeeper
            </span>
          </button>
        </div>

        <button
          onClick={() => onLogin(loginType)}
          className='w-full bg-blue-600 text-white py-4 text-lg rounded-lg hover:bg-blue-700 transition'
        >
          Login as {loginType === 'user' ? 'Citizen' : 'Shopkeeper'}
        </button>

        <div className='mt-8 pt-8 border-t'>
          <p className='text-center text-gray-600 mb-4'>Quick Demo Access</p>
          <div className='grid grid-cols-2 gap-4'>
            <button
              onClick={() => onLogin('user')}
              className='py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition'
            >
              Demo as Citizen
            </button>
            <button
              onClick={() => onLogin('admin')}
              className='py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition'
            >
              Demo as Shopkeeper
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
''')
print('✅ Created: src/pages/Login.jsx')

print('\\n🎉 ALL FILES CREATED SUCCESSFULLY!')
print('\\n🚀 NOW RUN: npm start')
print('\\n🌐 Open browser at: http://localhost:3000')


