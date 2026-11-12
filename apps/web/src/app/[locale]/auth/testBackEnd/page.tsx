'use client';

import { getRequest } from '@/api/api';

export default function TestingBackendPage() {

  const handleProfile = async () => {
    const result = await getRequest<unknown, unknown>('/auth/profile');
    console.log(result);
  };

  return (
    <div>
      <h1>Testing Backend</h1>
      <button onClick={handleProfile}>Get profile</button>
    </div>
  );
}
