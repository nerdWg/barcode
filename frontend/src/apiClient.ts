
export const fetchBinaryCode = async (code: string, type: string): Promise<string> => {
    const url = type === "ean8" ? "barcode8" : "barcode13";
    const response = await fetch(`/${url}/${code}`);
    return await response.text();
  };
  
  export const fetchBarCode = async (code: string, type: string): Promise<string> => {
    const url = type === "ean8" ? "bc8_svg" : "bc13_svg";
    const response = await fetch(`/${url}/${code}`);
    return await response.text();
  };
  