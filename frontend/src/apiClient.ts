import axios from "axios";

export const fetchBinaryCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = `/barcode/${type}/${code}`;
  const response = await axios.get(url, {
    headers: { Accept: "text/plain" },
  });
  return await response.data;
};

export const fetchBarCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = `/barcode/${type}/${code}`;
  const response = await axios.get(url, {
    headers: { Accept: "image/svg+xml" },
  });
  return await response.data;
};
