import { useState } from "react";
import AxiosClient from '../api/AxiosClient';

function UserForm() {
  const [fatherData, setFatherData] = useState({
    age: "", hb: "", hba2: "", hbf: "", mcv: "", mch: "", rbc: "", rdw: ""
  });

  const [motherData, setMotherData] = useState({
    age: "", hb: "", hba2: "", hbf: "", mcv: "", mch: "", rbc: "", rdw: ""
  });

  const [predictionResult, setPredictionResult] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);

  const handleInputChange = (e, person) => {
    const { name, value } = e.target;
    if (person === "father") {
      setFatherData({ ...fatherData, [name]: value });
    } else {
      setMotherData({ ...motherData, [name]: value });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const allFieldsFilled =
      Object.values(fatherData).every((val) => val !== "") &&
      Object.values(motherData).every((val) => val !== "");

    if (!allFieldsFilled) {
      setErrorMessage("Please fill in all fields for both father and mother.");
      setPredictionResult(null);
      return;
    }

    setIsLoading(true);
    try {
      const payload = { father: fatherData, mother: motherData };
      const response = await AxiosClient.post("/api/predict", payload);
      setPredictionResult(response.data.message || "Prediction complete.");
      setErrorMessage(null);
      setShowModal(true);
    } catch (error) {
      console.error("Frontend Error:", error);
      setErrorMessage(error.response?.data?.error || error.message);
      setPredictionResult(null);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setFatherData({ age: "", hb: "", hba2: "", hbf: "", mcv: "", mch: "", rbc: "", rdw: "" });
    setMotherData({ age: "", hb: "", hba2: "", hbf: "", mcv: "", mch: "", rbc: "", rdw: "" });
    setPredictionResult(null);
    setErrorMessage(null);
    setShowModal(false);
  };

  const closeModal = () => {
    setShowModal(false);
    setPredictionResult(null);
  };

  // Define ranges for each field
  const ranges = {
    age: { min: 20, max: 45 },
    hb: { min: 8, max: 15 },
    hba2: { min: 1, max: 10 },
    hbf: { min: 0, max: 10 },
    mcv: { min: 50, max: 100 },
    mch: { min: 27, max: 34 },
    rbc: { min: 3.8, max: 5.5 },
    rdw: { min: 11.5, max: 14.5 }
  };

  const renderInputs = (person, data) => (
    Object.keys(data).map((key) => (
      <div key={key} className="input-group">
        <label>{key.toUpperCase()}:</label>
        <input
          type="number"
          name={key}
          step="any"
          value={data[key]}
          onChange={(e) => handleInputChange(e, person)}
          min={ranges[key].min}
          max={ranges[key].max}
          required
        />
      </div>
    ))
  );

  return (
    <div className="prediction-form-wrapper">
      <div className={`prediction-form-container ${showModal ? 'blurred' : ''}`}>
        <form onSubmit={handleSubmit}>
          <fieldset>
            <legend>Father's Data</legend>
            <div className="input-grid">{renderInputs("father", fatherData)}</div>
          </fieldset>

          <fieldset>
            <legend>Mother's Data</legend>
            <div className="input-grid">{renderInputs("mother", motherData)}</div>
          </fieldset>

          <div className="button-group">
            <button type="submit" disabled={isLoading}>
              {isLoading ? "Predicting..." : "Predict"}
            </button>
            <button type="button" onClick={handleReset} disabled={isLoading}>
              Reset
            </button>
          </div>
        </form>

        {isLoading && (
          <div className="loading-container">
            <p>Loading...</p>
          </div>
        )}

        {errorMessage && (
          <div className="error-container">
            <p>{errorMessage}</p>
          </div>
        )}
      </div>

      {showModal && predictionResult && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Prediction Result</h3>
            <p>{predictionResult}</p>
            <button onClick={closeModal} className="modal-close-button">
              OK
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default UserForm