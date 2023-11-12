import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import SendFormData from './SendFormData';

const MyFormComponent = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ name: '', email: '' , spire: ''});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      SendFormData(formData)
      navigate('/results');
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name: 
        <input type="text" name="name" value={formData.name} onChange={handleChange} />
      </label>
      <br />
      <label>
        Email: 
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
      </label>
      <br />
      <label>
        SPIRE ID: 
        <input type="number" name="spire" value={formData.spire} onChange={handleChange} />
      </label>
      <br />
      <button type="submit">Sign In</button>
    </form>
  );
};

export default MyFormComponent;