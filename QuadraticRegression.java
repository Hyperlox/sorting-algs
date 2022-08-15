import java.lang.Math;

public class QuadraticRegression {
    double[] inputs, expected;
    private double a = 0;
    private final int numSteps = 10000000;
    final double delta = 0.01;

    public static void main(String args[]) {
        double[] inputs = new double[] { 100, 316, 1000, 3162, 10000, 31622, 100000 };
        double[] expected = new double[] { 589621, 2049144, 7528003, 26920245, 95076480, 399017799, 1600859283 };
        QuadraticRegression regression = new QuadraticRegression(inputs, expected);
        System.out.println("R^2: " + regression.rSquared());
    }

    public QuadraticRegression(double[] inputs, double[] expected) {
        if (inputs.length != expected.length) {
            throw new Error("Lengths are not equal");
        } else {
            this.inputs = inputs;
            this.expected = expected;
            double aPlus, aMinus;
            for (int i = 0; i < numSteps; i++) {
                aPlus = evaluate(a + delta, inputs, expected);
                aMinus = evaluate(a - delta, inputs, expected);
                if (aPlus < aMinus)
                    a += delta;
                else
                    a -= delta;
            }
        }
        System.out.println("Chi squared: " + evaluate(a, inputs, expected));
        System.out.println("Formula: y=" + a + "x^2");
    }

    private double evaluate(double a, double[] inputs, double[] expected) {
        if (inputs.length != expected.length) {
            throw new Error("Lengths are not equal");
        } else {
            double[] observed = new double[inputs.length];
            for (int i = 0; i < inputs.length; i++) {
                observed[i] = evaluateFunction(a, inputs[i]);
            }
            return chiSquared(expected, observed);
        }
    }

    private double evaluateFunction(double a, double n) {
        return a * Math.pow(n, 2);
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
            double predictedValue = evaluateFunction(a, value);
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
