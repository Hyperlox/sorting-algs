import java.lang.Math;

public class Regression {
    double[] inputs, expected;
    private double a = 0, b = 0;
    private final int numSteps = 10000;
    final double delta = 0.01;

    public static void main(String args[]) {
        double[] inputs = new double[] { 100, 316, 1000, 3162, 10000, 31622, 100000 };
        double[] expected = new double[] { 8062, 21841, 67103, 197560, 619524, 2134712, 8272710 };
        Regression regression = new Regression(inputs, expected);
        System.out.println("R^2: " + regression.rSquared());
    }

    public Regression(double[] inputs, double[] expected) {
        if (inputs.length != expected.length) {
            throw new Error("Lengths are not equal");
        } else {
            this.inputs = inputs;
            this.expected = expected;
            double aPlus, aMinus, bPlus, bMinus;
            for (int i = 0; i < numSteps; i++) {
                aPlus = evaluate(a + delta, b, inputs, expected);
                aMinus = evaluate(a - delta, b, inputs, expected);
                if (aPlus < aMinus)
                    a += delta;
                else
                    a -= delta;
                bPlus = evaluate(a, b + delta, inputs, expected);
                bMinus = evaluate(a, b - delta, inputs, expected);
                if (bPlus < bMinus)
                    b += delta;
                else
                    b -= delta;
            }
        }
        // System.out.println("Chi squared: " + evaluate(a, b, inputs, expected));
        System.out.println("a: " + a);
        System.out.println("b: " + b);
    }

    private double evaluate(double a, double b, double[] inputs, double[] expected) {
        if (inputs.length != expected.length) {
            throw new Error("Lengths are not equal");
        } else {
            double[] observed = new double[inputs.length];
            for (int i = 0; i < inputs.length; i++) {
                observed[i] = evaluateFunction(a, b, inputs[i]);
            }
            return chiSquared(expected, observed);
        }
    }

    private double evaluateFunction(double a, double b, double n) {
        return a * n * Math.log10(n) + b;
    }

    private double chiSquared(double[] expected, double[] observed) {
        if (expected.length != observed.length) {
            throw new Error("Lengths are not equal");
        } else {
            double chiSquared = 0;
            for (int i = 0; i < expected.length; i++) {
                double currentExpected = expected[i];
                double currentObserved = observed[i];
                double differenceSquared = java.lang.Math.pow(currentExpected - currentObserved, 2);
                chiSquared += differenceSquared / currentExpected;
            }
            return chiSquared;
        }
    }

    public double rSquared() {
        return 1 - sumSquaredResiduals() / sumSquaredTotal();
    }

    private double sumSquaredResiduals() {
        double total = 0;
        for (int i = 0; i < inputs.length; i++) {
            double value = inputs[i];
            double expectedValue = expected[i];
            double predictedValue = evaluateFunction(a, b, value);
            total += Math.pow(expectedValue - predictedValue, 2);
        }
        return total;
    }

    private double sumSquaredTotal() {
        double total = 0;
        double mean = mean(expected);
        for (int i = 0; i < inputs.length; i++) {
            total += Math.pow(expected[i] - mean, 2);
        }
        return total;
    }

    private double mean(double[] arr) {
        double total = 0;
        for (double val : arr) {
            total += val;
        }
        return total;
    }
}
