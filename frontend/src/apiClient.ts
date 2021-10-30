import axios from "axios";

export const fetchBinaryCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = type === "ean8" ? "barcode8" : "barcode13";
  const response = await axios.get(`/${url}/${code}`, {
    headers: { Accept: "text/plain" },
  });
  return await response.data;
};

export const fetchBarCode = async (
  code: string,
  type: string
): Promise<string> => {
  const url = type === "ean8" ? "barcode8" : "barcode13";
  const response = await axios.get(`/${url}/${code}`, {
    headers: { Accept: "image/svg+xml" },
  });
  return await response.data;
};
