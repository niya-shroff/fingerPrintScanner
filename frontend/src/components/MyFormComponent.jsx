import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Input } from 'react-form-component';
import SendFormData from './SendFormData';

const MyFormComponent = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ firstName: '', lastName: '', email: '', spire: ''});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    SendFormData(formData)
    navigate('/results');
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input onChange={handleChange}
        name='firstName'
        type='name'
        value={formData.spire}
        label='First Name'
      />
      <Input onChange={handleChange}
        name='lastName'
        type='name'
        value={formData.lastName}
        label='Last Name'
      />
      <Input onChange={handleChange}
        name='email'
        type='email'
        value={formData.email}
        label='E-mail Address'
      />
      <Input onChange={handleChange}
        name='spire'
        type='number'
        value={formData.spire}
        label='Spire ID'
      />
      <button type="submit">Save</button>
    </form>
  )
};

export default MyFormComponent;