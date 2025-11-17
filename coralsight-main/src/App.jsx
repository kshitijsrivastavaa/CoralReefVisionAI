import React, { useState } from 'react';
import { Camera, Upload, Activity, Info, Home } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [selectedImage, setSelectedImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState(null);

  const handleImageSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
      setResult(null);
    }
  };

  const handleAnalyze = async () => {
    if (!selectedImage) return;
    
    setAnalyzing(true);
    
    // Simulate API call - Replace this with actual backend API call later
    setTimeout(() => {
      // Mock result - this will be replaced with actual API response
      const mockResults = [
        {
          status: 'Healthy',
          confidence: 92.5,
          color: 'text-green-400',
          bgColor: 'bg-green-500/20',
          description: 'The coral reef appears healthy with vibrant colors and good structure.'
        },
        {
          status: 'Bleached',
          confidence: 87.3,
          color: 'text-yellow-400',
          bgColor: 'bg-yellow-500/20',
          description: 'Signs of coral bleaching detected. The reef shows loss of color due to stress.'
        },
        {
          status: 'Diseased',
          confidence: 78.9,
          color: 'text-red-400',
          bgColor: 'bg-red-500/20',
          description: 'Disease indicators detected. The reef shows signs of infection or illness.'
        },
        {
          status: 'Algae-Covered',
          confidence: 85.6,
          color: 'text-orange-400',
          bgColor: 'bg-orange-500/20',
          description: 'Excessive algae growth detected covering coral structures.'
        }
      ];
      
      setResult(mockResults[Math.floor(Math.random() * mockResults.length)]);
      setAnalyzing(false);
    }, 2000);
  };

  const renderHome = () => (
    <div className="text-center py-16">
      <div className="mb-8">
        <Camera className="w-20 h-20 text-cyan-400 mx-auto mb-4" />
        <h2 className="text-5xl font-bold text-white mb-4">CoralSight</h2>
        <p className="text-xl text-cyan-300 mb-2">AI-Powered Coral Reef Health Assessment</p>
        <p className="text-gray-300 max-w-2xl mx-auto">
          Upload coral reef images and get instant health assessments using our AI model
        </p>
      </div>
      
      <button
        onClick={() => setActiveTab('analyze')}
        className="bg-cyan-500 hover:bg-cyan-600 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-all transform hover:scale-105 shadow-lg"
      >
        Start Analysis
      </button>
    </div>
  );

  const renderAnalyze = () => (
    <div className="max-w-4xl mx-auto">
      <h2 className="text-3xl font-bold text-white mb-8 text-center">Analyze Coral Reef Image</h2>
      
      <div className="bg-white/5 backdrop-blur-lg rounded-2xl p-8 border border-cyan-500/20">
        {/* Upload Section */}
        <div className="mb-8">
          <label className="block mb-4">
            <div className="border-2 border-dashed border-cyan-500/50 rounded-lg p-8 text-center cursor-pointer hover:border-cyan-500 transition-all">
              <Upload className="w-12 h-12 text-cyan-400 mx-auto mb-3" />
              <p className="text-white font-semibold mb-2">Click to upload coral reef image</p>
              <p className="text-gray-400 text-sm">PNG, JPG up to 10MB</p>
              <input
                type="file"
                className="hidden"
                accept="image/*"
                onChange={handleImageSelect}
              />
            </div>
          </label>
        </div>

        {/* Image Preview */}
        {imagePreview && (
          <div className="mb-8">
            <h3 className="text-white font-semibold mb-3">Selected Image:</h3>
            <img
              src={imagePreview}
              alt="Coral preview"
              className="w-full max-h-96 object-contain rounded-lg border border-cyan-500/30"
            />
          </div>
        )}

        {/* Analyze Button */}
        {selectedImage && !result && (
          <button
            onClick={handleAnalyze}
            disabled={analyzing}
            className="w-full bg-cyan-500 hover:bg-cyan-600 disabled:bg-gray-600 text-white py-3 rounded-lg font-semibold transition-all"
          >
            {analyzing ? 'Analyzing...' : 'Analyze Image'}
          </button>
        )}

        {/* Results */}
        {result && (
          <div className="mt-8 space-y-6">
            <div className={`${result.bgColor} rounded-lg p-6 border border-cyan-500/30`}>
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-2xl font-bold text-white">Assessment Result</h3>
                <Activity className="w-8 h-8 text-cyan-400" />
              </div>
              
              <div className="space-y-4">
                <div>
                  <p className="text-gray-300 text-sm mb-1">Health Status:</p>
                  <p className={`text-3xl font-bold ${result.color}`}>{result.status}</p>
                </div>
                
                <div>
                  <p className="text-gray-300 text-sm mb-1">Confidence Level:</p>
                  <div className="flex items-center space-x-3">
                    <div className="flex-1 bg-gray-700 rounded-full h-3">
                      <div
                        className="bg-cyan-500 h-3 rounded-full transition-all"
                        style={{ width: `${result.confidence}%` }}
                      ></div>
                    </div>
                    <span className="text-white font-semibold">{result.confidence}%</span>
                  </div>
                </div>
                
                <div>
                  <p className="text-gray-300 text-sm mb-1">Description:</p>
                  <p className="text-white">{result.description}</p>
                </div>
              </div>
            </div>

            <button
              onClick={() => {
                setSelectedImage(null);
                setImagePreview(null);
                setResult(null);
              }}
              className="w-full bg-white/10 hover:bg-white/20 text-white py-3 rounded-lg font-semibold transition-all"
            >
              Analyze Another Image
            </button>
          </div>
        )}
      </div>
    </div>
  );

  const renderAbout = () => (
    <div className="max-w-4xl mx-auto">
      <h2 className="text-3xl font-bold text-white mb-8 text-center">About CoralSight</h2>
      
      <div className="bg-white/5 backdrop-blur-lg rounded-2xl p-8 border border-cyan-500/20 space-y-6">
        <div>
          <h3 className="text-xl font-bold text-cyan-400 mb-3">What is CoralSight?</h3>
          <p className="text-gray-300 leading-relaxed">
            CoralSight is a desktop-based AI/ML solution designed to automate coral reef health assessment. 
            Using advanced Convolutional Neural Networks (CNN), it analyzes coral reef images to determine 
            their health status without requiring internet connectivity.
          </p>
        </div>

        <div>
          <h3 className="text-xl font-bold text-cyan-400 mb-3">Classification Categories</h3>
          <div className="grid md:grid-cols-2 gap-4">
            {[
              { name: 'Healthy', color: 'green', desc: 'Vibrant, thriving coral' },
              { name: 'Bleached', color: 'yellow', desc: 'Loss of color due to stress' },
              { name: 'Diseased', color: 'red', desc: 'Signs of infection' },
              { name: 'Algae-Covered', color: 'orange', desc: 'Excessive algae growth' }
            ].map((cat) => (
              <div key={cat.name} className={`bg-${cat.color}-500/10 border border-${cat.color}-500/30 rounded-lg p-4`}>
                <p className={`text-${cat.color}-400 font-semibold mb-1`}>{cat.name}</p>
                <p className="text-gray-400 text-sm">{cat.desc}</p>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-xl font-bold text-cyan-400 mb-3">Key Features</h3>
          <ul className="space-y-2 text-gray-300">
            <li className="flex items-start">
              <span className="text-cyan-400 mr-2">•</span>
              <span>Fully offline processing - no internet required</span>
            </li>
            <li className="flex items-start">
              <span className="text-cyan-400 mr-2">•</span>
              <span>Pre-trained CNN model for accurate assessment</span>
            </li>
            <li className="flex items-start">
              <span className="text-cyan-400 mr-2">•</span>
              <span>Data privacy - all processing on local machine</span>
            </li>
            <li className="flex items-start">
              <span className="text-cyan-400 mr-2">•</span>
              <span>Accessible to researchers, conservationists, and students</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-teal-800 to-cyan-900">
      {/* Navigation */}
      <nav className="bg-blue-950/80 backdrop-blur-md sticky top-0 z-50 border-b border-cyan-500/20">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <Camera className="w-8 h-8 text-cyan-400" />
              <h1 className="text-2xl font-bold text-white">CoralSight</h1>
            </div>
            <div className="flex space-x-6">
              <button
                onClick={() => setActiveTab('home')}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                  activeTab === 'home'
                    ? 'bg-cyan-500/20 text-cyan-400'
                    : 'text-gray-300 hover:text-white'
                }`}
              >
                <Home className="w-5 h-5" />
                <span>Home</span>
              </button>
              <button
                onClick={() => setActiveTab('analyze')}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                  activeTab === 'analyze'
                    ? 'bg-cyan-500/20 text-cyan-400'
                    : 'text-gray-300 hover:text-white'
                }`}
              >
                <Activity className="w-5 h-5" />
                <span>Analyze</span>
              </button>
              <button
                onClick={() => setActiveTab('about')}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                  activeTab === 'about'
                    ? 'bg-cyan-500/20 text-cyan-400'
                    : 'text-gray-300 hover:text-white'
                }`}
              >
                <Info className="w-5 h-5" />
                <span>About</span>
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        {activeTab === 'home' && renderHome()}
        {activeTab === 'analyze' && renderAnalyze()}
        {activeTab === 'about' && renderAbout()}
      </main>

      {/* Footer */}
      <footer className="bg-blue-950/50 py-6 mt-12 border-t border-cyan-500/20">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p className="text-gray-400 text-sm">© 2025 CoralSight - Final Year Project</p>
        </div>
      </footer>
    </div>
  );
}
