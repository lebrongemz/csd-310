<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heat Energy Calculator</title>
</head>
<body>
    <script>
        // Function to calculate the energy needed to heat water
        function calculateHeatEnergy() {
            // Prompt user for the amount of water in kilograms
            let waterMass = parseFloat(prompt("Enter the amount of water in kilograms:"));
            
            // Check if waterMass is a valid number
            if (isNaN(waterMass) || waterMass <= 0) {
                alert("Please enter a valid positive number for the water mass.");
                return;
            }

            // Prompt user for the initial temperature
            let initialTemperature = parseFloat(prompt("Enter the initial temperature in Celsius:"));
            
            // Check if initialTemperature is a valid number
            if (isNaN(initialTemperature)) {
                alert("Please enter a valid number for the initial temperature.");
                return;
            }

            // Prompt user for the final temperature
            let finalTemperature = parseFloat(prompt("Enter the final temperature in Celsius:"));
            
            // Check if finalTemperature is a valid number
            if (isNaN(finalTemperature)) {
                alert("Please enter a valid number for the final temperature.");
                return;
            }

            // Calculate the energy needed using the formula
            const specificHeatCapacity = 4184; // in Joules per kilogram per degree Celsius
            let energyRequired = waterMass * (finalTemperature - initialTemperature) * specificHeatCapacity;

            // Display the result
            alert(`The energy required to heat the water is ${energyRequired.toFixed(2)} Joules.`);
        }

        // Call the function to execute the calculation
        calculateHeatEnergy();
    </script>
</body>
</html>