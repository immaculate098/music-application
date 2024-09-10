import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import Library from './components/Library';
import { AuthProvider } from '../AuthContext';
import { AudioProvider } from '../AudioContext';
import axios from 'axios';

jest.mock('axios');

describe('Library Component', () => {
  beforeEach(() => {
    axios.get.mockResolvedValue({
      data: [
        { id: 1, title: 'Test Song', artist: 'Test Artist', duration: '3:30' }
      ]
    });
  });

  test('renders Library component', async () => {
    render(
      <AuthProvider>
        <AudioProvider>
          <Library />
        </AudioProvider>
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Library')).toBeInTheDocument();
      expect(screen.getByText('Top music')).toBeInTheDocument();
      expect(screen.getByText('Playlist')).toBeInTheDocument();
    });
  });

  test('displays songs in the playlist', async () => {
    render(
      <AuthProvider>
        <AudioProvider>
          <Library />
        </AudioProvider>
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Test Song')).toBeInTheDocument();
      expect(screen.getByText('Test Artist')).toBeInTheDocument();
    });
  });
});